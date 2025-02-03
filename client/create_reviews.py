import requests
import random

def main():
    # 1) Obtain JWT Token
    token_url = "http://127.0.0.1:8000/api/token/"
    login_data = {
        "username": "admin",
        "password": "admin"
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

    for i in range(10):
        # Choose a random course ID between 0 and 32
        course_id = random.randint(0, 32)
        # Choose a random rating between 0 and 5
        rating = random.randint(0, 5)

        review_data = {
            "user": 7,
            "course": course_id,
            "rating": rating,
            "content": f"Auto-generated review #{i+1} for course {course_id}."
        }

        create_response = requests.post(reviews_url, json=review_data, headers=headers)
        if create_response.status_code == 201:
            print(f"Review #{i+1} created successfully:", create_response.json())
        else:
            print(f"Failed to create review #{i+1}:", create_response.text)

if __name__ == "__main__":
    main()
