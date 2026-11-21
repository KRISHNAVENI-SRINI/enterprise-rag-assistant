import requests
from config import GEMINI_API_KEY

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-lite-latest:generateContent?key={GEMINI_API_KEY}"

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "What is RAG?"
                }
            ]
        }
    ]
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())