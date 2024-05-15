import json
import os
import pandas as pd
import requests as req

# Get the base URL from environment variable
base_url = os.getenv('GITHUB_API_BASE_URL', 'https://api.github.com')

def get_sbom_url(owner, repo):
    return f"{base_url}/repos/{owner}/{repo}/dependency-graph/sbom"

def generate_sbom_csv():
    """
    Generate SBOM CSV file from GitHub repositories.

    This function prompts the user to enter the GitHub organization name, repository names (separated by commas),
    and GitHub token. It then retrieves the SBOM (Software Bill of Materials) for each repository using the GitHub API,
    processes the JSON data, and saves the relevant information to a CSV file named 'SBOM.csv'. The function 
    eventually skips packages with 'github' in the name and saves the processed data to a CSV file with specific columns.

    Returns:
        None
    """
    githuborg =  input("\nPlease enter the GitHub organization name: ")
    githubrepo = input("\nPlease input the GitHub repository names, separated by commas: ")
    githubtoken = input("\nPlease enter your GitHub token: ")
    csvfilename = 'SBOM.csv'
    
    repos = githubrepo.split(",")
    newdf = pd.DataFrame()

    for repo in repos:
        # API endpoint URL
        url = get_sbom_url(githuborg, repo)

        # Headers for the request
        headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': 'Bearer {}'.format(githubtoken),
            'X-GitHub-Api-Version': '2022-11-28'
        }

        # Send GET request to the API
        response = req.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the JSON data from the response
            sbomjson = json.loads(response.text)
            
            # Load JSON data from sbom>packages node
            packagesjson = sbomjson['sbom']['packages']

            # Convert packages json to dataframe
            df = pd.DataFrame(data=packagesjson)
            df['Repository Name'] = repo
            newdf = pd.concat([newdf, df])
        else:
            print('Failed to fetch SBOM from the API. Status code:', response.status_code)

    # Skip packages having github in the name
    finaldf = newdf[~newdf["name"].str.contains("github")]
    
    #finaldf["name"] = finaldf["name"].str.split(":", n=1).str[1]
    
    # Rename name column
    finaldf = finaldf.rename(columns={"name": "Package Name"})
    
    finaldf.to_csv(csvfilename, index=False, columns="Repository Name,Package Name,SPDXID,versionInfo,licenseConcluded,supplier".split(","))

generate_sbom_csv()
