import requests

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
headers = {"Authorization": "Bearer YOUR_API_KEY"}

def query(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    return response.json()

print(query("Explain AI simply"))
print(query("Write a short story about a robot"))
print(query("Give 3 study tips for college students"))
