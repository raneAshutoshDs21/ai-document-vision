import requests

BACKEND_URL = "http://127.0.0.1:8000"

def analyze_document(file):
    url = f"{BACKEND_URL}/analyze"
    files = {"file": (file.name, file, file.type)}

    response = requests.post(url, files=files)
    response.raise_for_status()
    return response.json()
