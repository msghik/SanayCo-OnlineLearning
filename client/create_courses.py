import requests

# Endpoint URLs
LOGIN_URL = "http://127.0.0.1:8000/api/token/"
COURSES_URL = "http://127.0.0.1:8000/courses/create/"

# Credentials for the instructor user (must be an instructor)
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

# Define 20 courses (2 courses per category for 10 categories)
# In each course, we include:
# - title, description, price, is_published, category (id), video path
# - instructor (set to 7, for example) and a list of student ids in "users"
courses_data = [
    # Category 1: Science
    {
        "title": "Fundamentals of Physics",
        "description": "An introductory course on the principles of physics.",
        "price": "29.99",
        "is_published": True,
        "category": 1,
        "video": "/mnt/c/Videos/physics_intro.mp4",
        "instructor": 3,
        "users": [5,6]
    },
    {
        "title": "Chemistry Essentials",
        "description": "Learn the basics of chemistry and chemical reactions.",
        "price": "24.99",
        "is_published": True,
        "category": 1,
        "video": "/mnt/c/Videos/chemistry_essentials.mp4",
        "instructor": 2,
        "users": [2]
    },
    # Category 2: Technology
    {
        "title": "Introduction to Programming",
        "description": "Learn the fundamentals of programming with Python.",
        "price": "34.99",
        "is_published": True,
        "category": 2,
        "video": "/mnt/c/Videos/programming_intro.mp4",
        "instructor": 2,
        "users": []
    },
    {
        "title": "Web Development Bootcamp",
        "description": "A comprehensive course on HTML, CSS, and JavaScript.",
        "price": "39.99",
        "is_published": True,
        "category": 2,
        "video": "/mnt/c/Videos/web_development_bootcamp.mp4",
        "instructor": 3,
        "users": []
    },
    # Category 3: Engineering
    {
        "title": "Mechanical Engineering Basics",
        "description": "An overview of mechanical engineering principles.",
        "price": "44.99",
        "is_published": True,
        "category": 3,
        "video": "/mnt/c/Videos/mechanical_engineering.mp4",
        "instructor": 3,
        "users": [5,6]
    },
    {
        "title": "Electrical Circuits 101",
        "description": "Learn the fundamentals of electrical circuits.",
        "price": "39.99",
        "is_published": True,
        "category": 3,
        "video": "/mnt/c/Videos/electrical_circuits.mp4",
        "instructor": 3,
        "users": []
    },
    # Category 4: Mathematics
    {
        "title": "Calculus for Beginners",
        "description": "An introduction to limits, derivatives, and integrals.",
        "price": "29.99",
        "is_published": True,
        "category": 4,
        "video": "/mnt/c/Videos/calculus_for_beginners.mp4",
        "instructor": 2,
        "users": [1]
    },
    {
        "title": "Statistics and Probability",
        "description": "Learn the basics of statistics and probability theory.",
        "price": "34.99",
        "is_published": True,
        "category": 4,
        "video": "/mnt/c/Videos/statistics_probability.mp4",
        "instructor": 2,
        "users": [8]
    },
    # Category 5: Arts
    {
        "title": "Introduction to Painting",
        "description": "Explore painting techniques and art styles.",
        "price": "19.99",
        "is_published": True,
        "category": 5,
        "video": "/mnt/c/Videos/intro_to_painting.mp4",
        "instructor": 3,
        "users": [4]
    },
    {
        "title": "Digital Photography",
        "description": "Learn how to take and edit beautiful photos.",
        "price": "24.99",
        "is_published": True,
        "category": 5,
        "video": "/mnt/c/Videos/digital_photography.mp4",
        "instructor": 2,
        "users": [6]
    },
    # Category 6: History
    {
        "title": "World History Overview",
        "description": "A survey of major events in world history.",
        "price": "29.99",
        "is_published": True,
        "category": 6,
        "video": "/mnt/c/Videos/world_history_overview.mp4",
        "instructor": 3,
        "users": []
    },
    {
        "title": "Ancient Civilizations",
        "description": "Explore the history and culture of ancient societies.",
        "price": "34.99",
        "is_published": True,
        "category": 6,
        "video": "/mnt/c/Videos/ancient_civilizations.mp4",
        "instructor": 2,
        "users": []
    },
    # Category 7: Business
    {
        "title": "Entrepreneurship 101",
        "description": "Learn how to start and run your own business.",
        "price": "39.99",
        "is_published": True,
        "category": 7,
        "video": "/mnt/c/Videos/entrepreneurship_101.mp4",
        "instructor": 3,
        "users": []
    },
    {
        "title": "Financial Management",
        "description": "A course on budgeting, investing, and financial planning.",
        "price": "34.99",
        "is_published": True,
        "category": 7,
        "video": "/mnt/c/Videos/financial_management.mp4",
        "instructor": 3,
        "users": [5]
    },
    # Category 8: Health
    {
        "title": "Nutrition and Wellness",
        "description": "Learn about nutrition and maintaining a healthy lifestyle.",
        "price": "24.99",
        "is_published": True,
        "category": 8,
        "video": "/mnt/c/Videos/nutrition_wellness.mp4",
        "instructor": 3,
        "users": [5]
    },
    {
        "title": "Yoga and Mindfulness",
        "description": "Techniques for stress relief and mindfulness through yoga.",
        "price": "19.99",
        "is_published": True,
        "category": 8,
        "video": "/mnt/c/Videos/yoga_mindfulness.mp4",
        "instructor": 2,
        "users": [6,5]
    },
    # Category 9: Education
    {
        "title": "Effective Teaching Strategies",
        "description": "Learn methods and techniques for effective teaching.",
        "price": "29.99",
        "is_published": True,
        "category": 9,
        "video": "/mnt/c/Videos/effective_teaching.mp4",
        "instructor": 2,
        "users": [5, 6]
    },
    {
        "title": "Curriculum Development",
        "description": "An in-depth course on designing educational curricula.",
        "price": "34.99",
        "is_published": True,
        "category": 9,
        "video": "/mnt/c/Videos/curriculum_development.mp4",
        "instructor": 2,
        "users": [3, 5]
    },
    # Category 10: Lifestyle
    {
        "title": "Personal Development",
        "description": "Focus on self-improvement, productivity, and goal-setting.",
        "price": "24.99",
        "is_published": True,
        "category": 10,
        "video": "/mnt/c/Videos/personal_development.mp4",
        "instructor": 2,
        "users": [1]
    },
    {
        "title": "Travel and Culture",
        "description": "Explore different cultures and gain travel insights.",
        "price": "19.99",
        "is_published": True,
        "category": 10,
        "video": "/mnt/c/Videos/travel_culture.mp4",
        "instructor": 2,
        "users": [2]
    }
]

def create_course(token, course):
    """Send a POST request to create a course using the given token and course data."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    response = requests.post(COURSES_URL, json=course, headers=headers)
    if response.status_code in [200, 201]:
        print(f"✅ Course '{course['title']}' created successfully.")
    else:
        print(f"❌ Failed to create course '{course['title']}': {response.text}")

def main():
    token = login_and_get_token()
    if not token:
        return

    for course in courses_data:
        create_course(token, course)

if __name__ == "__main__":
    main()
