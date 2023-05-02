import requests

response = requests.get('http://localhost')
print(response.status_code)
