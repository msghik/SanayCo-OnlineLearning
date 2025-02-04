import requests
import json

# --- Endpoint URLs ---
REGISTER_URL = "http://127.0.0.1:8000/accounts/register_user/"
LOGIN_URL    = "http://127.0.0.1:8000/api/token/"
COURSES_URL  = "http://127.0.0.1:8000/courses/"

# --- Data for the new instructor user ---
new_user_data = {
    "first_name": "Test",
    "last_name": "Instructor",
    "username": "testinstructor",
    "phone_number": "09123456789",  # 11 digits
    "email": "test.instructor@example.com",
    "password": "Password123!",
    "role": "instructor"  # Ensure role is correct as expected by your system
}

def sign_up_user(user_data):
    print("Signing up new user...")
    response = requests.post(REGISTER_URL, json=user_data)
    if response.status_code in [200, 201]:
        print("✅ Sign-up successful.")
        return True
    else:
        print("❌ Sign-up failed:", response.text)
        return False

def login_and_get_token(credentials):
    print("Logging in user...")
    response = requests.post(LOGIN_URL, json=credentials)
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data.get("access")
        print("✅ Login successful. Access token retrieved:")
        print(access_token)
        return access_token
    else:
        print("❌ Login failed:", response.text)
        return None

def create_course(token, course_data):
    print("Creating course...")
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.post(COURSES_URL+'create/', json=course_data, headers=headers)
    if response.status_code in [200, 201]:
        course = response.json()
        print("✅ Course created successfully.")
        print("Course ID:", course.get("id"))
        return course.get("id")
    else:
        print("❌ Failed to create course:", response.text)
        return None

def update_course(token, course_id, updated_data):
    print("Updating course...")
    url = f"{COURSES_URL}{course_id}/"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.put(url, json=updated_data, headers=headers)
    if response.status_code in [200, 201]:
        print("✅ Course updated successfully.")
        updated_course = response.json()
        print("Updated Title:", updated_course.get("title"))
        return True
    else:
        print("❌ Failed to update course:", response.text)
        return False

def delete_course(token, course_id):
    print("Deleting course...")
    url = f"{COURSES_URL}{course_id}/"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print("✅ Course deleted successfully.")
        return True
    else:
        print("❌ Failed to delete course:", response.text)
        return False

def main():
    # 1. Sign up the new instructor
    if not sign_up_user(new_user_data):
        print("User sign-up failed. Exiting.")
        return

    # 2. Log in with the newly registered user
    credentials = {
        "username": new_user_data["username"],
        "password": new_user_data["password"]
    }
    token = login_and_get_token(credentials)
    if not token:
        print("Unable to retrieve token. Exiting.")
        return

    # 3. Create a new course using the instructor's token
    # (Assume category 1 exists; assign some student ids in the "users" list)
    course_data = {
        "title": "Advanced Python Programming",
        "description": "An in-depth course covering advanced Python topics.",
        "price": "49.99",
        "is_published": True,
        "category": 1,          # category id (adjust if necessary)
        "video": "/mnt/c/Videos/advanced_python.mp4",
        "instructor": 3,  # We'll override it on the server side if your endpoint sets instructor automatically.
                         # Otherwise, you can set it to the new instructor's id if known.
        "users": [1, 2, 3]  # Example student ids
    }
    course_id = create_course(token, course_data)
    if not course_id:
        print("Course creation failed. Exiting.")
        return

    # 4. Update the course - for example, change the title and description
    updated_course_data = {
        "title": "Advanced Python Programming - Updated",
        "description": "An updated description covering advanced Python topics with new examples.",
        "price": "49.99",
        "is_published": True,
        "category": 1,
        "video": "/mnt/c/Videos/advanced_python_updated.mp4",
        "instructor": 0,  # same note as above
        "users": [11, 12, 13]
    }
    update_success = update_course(token, course_id, updated_course_data)
    if not update_success:
        print("Course update failed. Exiting.")
        return

    # 5. Delete the course
    delete_course(token, course_id)

if __name__ == "__main__":
    main()
