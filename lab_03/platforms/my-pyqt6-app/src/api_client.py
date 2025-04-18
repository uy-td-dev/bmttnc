import requests

def call_api(url, payload):
    try:
        res = requests.post(url, json=payload)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print(f"API error: {e}")
        return None
