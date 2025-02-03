import requests

# URL for obtaining JWT tokens
LOGIN_URL = "http://127.0.0.1:8000/api/token/"

# Predefined list of users (usernames) with the known common password
users = [
    {"username": "johndoe", "password": "Password123!"},
    {"username": "janesmith", "password": "Password123!"},
    {"username": "michaeljohnson", "password": "Password123!"},
    {"username": "emilydavis", "password": "Password123!"},
    {"username": "davidwilson", "password": "Password123!"},
    {"username": "sarahbrown", "password": "Password123!"},
    {"username": "robertmiller", "password": "Password123!"},
    {"username": "lindataylor", "password": "Password123!"},
    {"username": "jamesanderson", "password": "Password123!"},
    {"username": "karenthomas", "password": "Password123!"}
]

def login_and_get_token(user):
    payload = {
        "username": user["username"],
        "password": user["password"]
    }
    
    response = requests.post(LOGIN_URL, json=payload)
    
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data.get("access")
        print(f"✅ User '{user['username']}' logged in successfully. Token: {access_token}")
    else:
        print(f"❌ Failed to login user '{user['username']}': {response.text}")

def main():
    for user in users:
        login_and_get_token(user)

if __name__ == "__main__":
    main()
