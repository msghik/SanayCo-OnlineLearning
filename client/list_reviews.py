import requests
import random

def main():
    token_url = "http://127.0.0.1:8000/api/token/"
    login_data = {
        "username": "7",
        "password": "7"
    }

    token_response = requests.post(token_url, json=login_data)
    if token_response.status_code != 200:
        print("Failed to obtain token:", token_response.text)
        return

    tokens = token_response.json()
    access_token = tokens["access"]  # Use the 'access' token to authorize requests

    # 2) Create 10 Reviews
    reviews_url = "http://127.0.0.1:8000/reviews/"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url= reviews_url, headers=headers)
    print(response.json())

if __name__ == "__main__":
    main()
