import requests
import random

# API endpoint for registering users
REGISTER_URL = "http://127.0.0.1:8000/accounts/register_user/"

# List of available roles
ROLES = ["admin", "instructor", "student"]

# Predefined list of users with realistic names, 11-digit phone numbers, and emails
users = [
    {
        "first_name": "John", 
        "last_name": "Doe", 
        "username": "johndoe", 
        "phone_number": "07123456789",
        "email": "john.doe@example.com"
    },
    {
        "first_name": "Jane", 
        "last_name": "Smith", 
        "username": "janesmith", 
        "phone_number": "07234567890",
        "email": "jane.smith@example.com"
    },
    {
        "first_name": "Michael", 
        "last_name": "Johnson", 
        "username": "michaeljohnson", 
        "phone_number": "07345678901",
        "email": "michael.johnson@example.com"
    },
    {
        "first_name": "Emily", 
        "last_name": "Davis", 
        "username": "emilydavis", 
        "phone_number": "07456789012",
        "email": "emily.davis@example.com"
    },
    {
        "first_name": "David", 
        "last_name": "Wilson", 
        "username": "davidwilson", 
        "phone_number": "07567890123",
        "email": "david.wilson@example.com"
    },
    {
        "first_name": "Sarah", 
        "last_name": "Brown", 
        "username": "sarahbrown", 
        "phone_number": "07678901234",
        "email": "sarah.brown@example.com"
    },
    {
        "first_name": "Robert", 
        "last_name": "Miller", 
        "username": "robertmiller", 
        "phone_number": "07789012345",
        "email": "robert.miller@example.com"
    },
    {
        "first_name": "Linda", 
        "last_name": "Taylor", 
        "username": "lindataylor", 
        "phone_number": "07890123456",
        "email": "linda.taylor@example.com"
    },
    {
        "first_name": "James", 
        "last_name": "Anderson", 
        "username": "jamesanderson", 
        "phone_number": "07901234567",
        "email": "james.anderson@example.com"
    },
    {
        "first_name": "Karen", 
        "last_name": "Thomas", 
        "username": "karenthomas", 
        "phone_number": "07012345678",
        "email": "karen.thomas@example.com"
    }
]

# Common password for all users
PASSWORD = "Password123!"

def create_user(user):
    # Prepare the data for the POST request
    user_data = {
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "username": user["username"],
        "phone_number": user["phone_number"],
        "email": user["email"],
        "password": PASSWORD,
        "role": random.choice(ROLES)
    }
    
    # Send the POST request to create the user
    response = requests.post(REGISTER_URL, json=user_data)
    
    if response.status_code == 201:
        print(f"✅ User {user_data['username']} created successfully with role {user_data['role']}.")
    else:
        print(f"❌ Failed to create user {user_data['username']}: {response.text}")

def main():
    for user in users:
        create_user(user)

if __name__ == "__main__":
    main()
