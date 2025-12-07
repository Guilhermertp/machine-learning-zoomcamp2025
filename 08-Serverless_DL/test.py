import requests

# URL of the Lambda container
lambda_url = "http://localhost:9000/2015-03-31/functions/function/invocations"

# Payload sent to your Lambda function
data = {"url": "http://bit.ly/mlbookcamp-pants"}

# Send POST request
response = requests.post(lambda_url, json=data)

# Print raw response first (to debug)
print("Status code:", response.status_code)
print("Response text:", response.text)

# Try parsing JSON if container returned valid JSON
try:
    result = response.json()
    print("Parsed JSON:", result)
except Exception as e:
    print("Failed to parse JSON:", e)
