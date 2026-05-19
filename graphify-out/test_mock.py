import requests
import json

url = "http://localhost:8080/v1/messages"
headers = {
    "x-api-key": "test",
    "content-type": "application/json"
}
payload = {
    "model": "claude-3-5-sonnet-20241022",
    "max_tokens": 1024,
    "messages": [
        {"role": "user", "content": "Hello, respond with a short JSON containing a single field 'status': 'ok'."}
    ]
}

try:
    response = requests.post(url, json=payload, headers=headers)
    print("Messages endpoint status:", response.status_code)
    print("Messages endpoint response:", response.text)
except Exception as e:
    print("Messages endpoint failed:", e)

url_chat = "http://localhost:8080/v1/chat/completions"
payload_chat = {
    "model": "gpt-4",
    "messages": [
        {"role": "user", "content": "Hello"}
    ]
}
try:
    response = requests.post(url_chat, json=payload_chat, headers=headers)
    print("Chat completions status:", response.status_code)
    print("Chat completions response:", response.text)
except Exception as e:
    print("Chat completions failed:", e)
