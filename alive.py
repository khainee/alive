import requests

response = requests.get('http://127.0.0.1')
print(response.status_code)
