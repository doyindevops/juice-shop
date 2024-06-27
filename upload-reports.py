import requests
import sys

file_name = sys.argv[1]
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
else:
    print(f'Unsupported scan type for file: {file_name}')
    sys.exit(1)

headers = {
    'Authorization': 'Token YOUR_DEFECTDOJO_API_TOKEN'  # Replace with your actual token or use environment variable
}

url = 'https://demo.defectdojo.org/api/v2/import-scan/'

data = {
    'active': True,
    'verified': True,
    'scan_type': scan_type,
    'minimum_severity': 'Low',
    'engagement': 14  # Replace with your actual engagement ID
}

files = {
    'file': open(file_name, 'rb')
}

try:
    response = requests.post(url, headers=headers, data=data, files=files, verify=False)  # Disable SSL verification
    response.raise_for_status()
    if response.status_code == 201:
        print('Scan results imported successfully')
    else:
        print(f'Failed to import scan results: {response.content}')
except requests.exceptions.RequestException as e:
    print(f'Error: {e}')
    print(f'Response: {e.response.content}' if e.response else 'No response content')
    sys.exit(1)
finally:
    files['file'].close()
