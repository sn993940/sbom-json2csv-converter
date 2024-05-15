# sbom-json2csv-converter

This repository hosts a tool designed to facilitate the conversion of Software Bill of Materials (SBOM) data from JSON format into CSV format. This tool processes dependency graphs downloaded from GitHub repositories with SPDX specification

## Key Features:

- Converts SBOM data from JSON to CSV format.
- Processes dependency graphs downloaded from GitHub repositories with SPDX specification.
- Maintains data integrity and structure during conversion.
- Supports customization options for CSV output.
- Lightweight and easy-to-use command-line interface.
- Suitable for integration into automated pipelines or manual usage.

Whether you're a software developer, system administrator, or security professional, the SBOM-JSON2CSV-Converter empowers you to efficiently manage and analyze software component data in a structured and accessible manner, while seamlessly incorporating dependency graphs from GitHub repositories.

## Input requirements

- GitHub Organization Name
- GitHub Repository Names(separated by comma)
- GitHub Personal Access Token(Refer https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on/authorizing-a-personal-access-token-for-use-with-saml-single-sign-on)

## Usage
Run generate_sbom_csv.py in console and provide above inputs to generate SBOM
