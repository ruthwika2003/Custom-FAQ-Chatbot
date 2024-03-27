import requests
import json

url = "http://localhost:11434/api/generate"

headers = {
    'Content-type': 'application/json',
}

data = {
    "model": "mistral",
    "prompt": "Why is mental health important?"
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print(response.text)

else:
    print("Error:", response.status_code, response.text)