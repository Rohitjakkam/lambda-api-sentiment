import requests

url = "<your-api-url/add-stage>/predict"
headers = {"Content-Type": "application/json"}
data = {"text": "I regret buying this laptop; it keeps freezing and the battery drains too fast."}

response = requests.post(url, headers=headers, json=data)  # ✅ JSON format
print(response.json())  # Expected output: {"sentiment": "POSITIVE"}
