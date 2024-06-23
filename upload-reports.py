import requests
import sys
import os

def upload_report(file_name):
    scan_type = ''

    if file_name == 'gitleaks.json':
        scan_type = 'Gitleaks Scan'
    elif file_name == 'njsscan.sarif':
        scan_type = 'SARIF'
    elif file_name == 'semgrep.json':
        scan_type = 'Semgrep JSON Report'
    elif file_name == 'retire.json':
        scan_type = 'Retire.js Scan'
    elif file_name == 'trivy.json':
        scan_type = 'Trivy Scan'

    headers = {
        'Authorization': f'Token {os.environ["DEFECTDOJO_API_TOKEN"]}'
    }

    url = 'https://demo.defectdojo.org/api/v2/import-scan/'

    data = {
        'active': True,
        'verified': True,
        'scan_type': scan_type,
        'minimum_severity': 'Low',
        'engagement': 4  # Replace with your actual engagement ID
    }

    files = {
        'file': open(file_name, 'rb')
    }

    response = requests.post(url, headers=headers, data=data, files=files)

    if response.status_code == 201:
        print('Scan results imported successfully')
    else:
        print(f'Failed to import scan results: {response.content}')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python upload-reports.py <report_file>")
        sys.exit(1)

    report_file = sys.argv[1]
    upload_report(report_file)
