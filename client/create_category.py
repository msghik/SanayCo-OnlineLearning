import requests

# Endpoint URLs
LOGIN_URL = "http://127.0.0.1:8000/api/token/"
CATEGORIES_URL = "http://127.0.0.1:8000/categories/"

# Credentials for the user we will log in with
user_credentials = {
    "username": "admin",
    "password": "admin"
}

# List of meaningful categories with names and descriptions
categories = [
    {"name": "Science", "description": "Courses related to scientific studies and research."},
    {"name": "Technology", "description": "Courses covering the latest tech trends and innovations."},
    {"name": "Engineering", "description": "Courses on engineering principles, design, and innovation."},
    {"name": "Mathematics", "description": "Courses focusing on mathematics, statistics, and logic."},
    {"name": "Arts", "description": "Courses covering various forms of visual, performing, and literary arts."},
    {"name": "History", "description": "Courses that explore historical events and cultures."},
    {"name": "Business", "description": "Courses on entrepreneurship, management, and financial literacy."},
    {"name": "Health", "description": "Courses on healthcare, nutrition, and wellness."},
    {"name": "Education", "description": "Courses that address teaching methodologies and educational theory."},
    {"name": "Lifestyle", "description": "Courses related to personal development, travel, and leisure."}
]

def login_and_get_token():
    """Log in with a user and return the JWT access token."""
    response = requests.post(LOGIN_URL, json=user_credentials)
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data.get("access")
        print(f"Logged in as {user_credentials['username']}. Token: {access_token}")
        return access_token
    else:
        print("Login failed:", response.text)
        return None

def create_category(token, name, description):
    """Create a category using the provided token."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "name": name,
        "description": description
    }
    response = requests.post(CATEGORIES_URL, json=payload, headers=headers)
    if response.status_code in [200, 201]:
        print(f"Category '{name}' created successfully.")
    else:
        print(f"Failed to create category '{name}': {response.text}")

def main():
    token = login_and_get_token()
    if not token:
        return

    # Create the meaningful categories
    for category in categories:
        create_category(token, category["name"], category["description"])

if __name__ == "__main__":
    main()
