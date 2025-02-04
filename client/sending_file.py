import requests

course_id = 5
LOGIN_URL = "http://127.0.0.1:8000/api/token/"
url = f"http://127.0.0.1:8000/courses/{course_id}/upload-video/"

user_credentials = {
    "username": "admin",
    "password": "admin"
}

def login_and_get_token():
    """Log in and return the JWT access token."""
    response = requests.post(LOGIN_URL, json=user_credentials)
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data.get("access")
        print(f"Logged in as {user_credentials['username']}. Token: {access_token}")
        return access_token
    else:
        print("Login failed:", response.text)
        return None
    

token = login_and_get_token()

headers = {
    "Authorization": f"Bearer {token}"
}


files = {
    "video": open("/home/msghol/home/msghol/SanayCo/mysite/video.mp4", "rb")
}

response = requests.post(url, headers=headers, files=files)


print("Status Code:", response.status_code)
print("Response:", response.json())
