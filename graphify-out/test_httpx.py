import os
import requests

url = "https://api.anthropic.com/v1/messages"
headers = {
    "x-api-key": os.environ.get("ANTHROPIC_AUTH_TOKEN", ""),
    "anthropic-version": "2023-06-01",
    "content-type": "application/json"
}
payload = {
    "model": "claude-3-5-sonnet-20241022",
    "max_tokens": 100,
    "messages": [
        {"role": "user", "content": "Hello"}
    ]
}

print("Headers keys:", list(headers.keys()))
print("Auth token starts with:", os.environ.get("ANTHROPIC_AUTH_TOKEN", "")[:10])

try:
    response = requests.post(url, json=payload, headers=headers)
    print("Status:", response.status_code)
    print("Response:", response.text)
except Exception as e:
    import traceback
    traceback.print_exc()
