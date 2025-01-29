import requests

BASE_URL = "http://127.0.0.1:8000"  # or your server URL

# 1. Student Sign-Up
def test_student_signup(data):
    url = f"{BASE_URL}/accounts/signup/student/"

    response = requests.post(url, json=data)

    print("\n-- Student Sign-Up --")
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
    
data_list = [
    {"phone_number": "3", "email": "student1@example.com", "password": "studentPass123", "full_name": "John Student", "course": "Computer Science", "enrollment_number": "STU-101"},
    {"phone_number": "4", "email": "student2@example.com", "password": "studentPass123", "full_name": "Jane Doe", "course": "Mathematics", "enrollment_number": "STU-102"},
    {"phone_number": "5", "email": "student3@example.com", "password": "studentPass123", "full_name": "Alex Kim", "course": "Physics", "enrollment_number": "STU-103"},
    {"phone_number": "6", "email": "student4@example.com", "password": "studentPass123", "full_name": "Emily Johnson", "course": "Biology", "enrollment_number": "STU-104"},
    {"phone_number": "7", "email": "student5@example.com", "password": "studentPass123", "full_name": "Chris Lee", "course": "Chemistry", "enrollment_number": "STU-105"},
    {"phone_number": "8", "email": "student6@example.com", "password": "studentPass123", "full_name": "Sarah White", "course": "Philosophy", "enrollment_number": "STU-106"},
    {"phone_number": "9", "email": "student7@example.com", "password": "studentPass123", "full_name": "David Smith", "course": "Economics", "enrollment_number": "STU-107"},
    {"phone_number": "10", "email": "student8@example.com", "password": "studentPass123", "full_name": "Laura Green", "course": "History", "enrollment_number": "STU-108"},
    {"phone_number": "11", "email": "student9@example.com", "password": "studentPass123", "full_name": "Michael Davis", "course": "Engineering", "enrollment_number": "STU-109"},
    {"phone_number": "12", "email": "student10@example.com", "password": "studentPass123", "full_name": "Rachel Clark", "course": "Literature", "enrollment_number": "STU-110"},
    {"phone_number": "13", "email": "student11@example.com", "password": "studentPass123", "full_name": "Sophie Taylor", "course": "Psychology", "enrollment_number": "STU-111"},
    {"phone_number": "14", "email": "student12@example.com", "password": "studentPass123", "full_name": "James Robinson", "course": "Art History", "enrollment_number": "STU-112"},
    {"phone_number": "15", "email": "student13@example.com", "password": "studentPass123", "full_name": "Linda Martinez", "course": "Sociology", "enrollment_number": "STU-113"},
    {"phone_number": "16", "email": "student14@example.com", "password": "studentPass123", "full_name": "Benjamin Wilson", "course": "Political Science", "enrollment_number": "STU-114"},
    {"phone_number": "17", "email": "student15@example.com", "password": "studentPass123", "full_name": "Olivia Moore", "course": "Law", "enrollment_number": "STU-115"},
    {"phone_number": "18", "email": "student16@example.com", "password": "studentPass123", "full_name": "Jack Harris", "course": "Nursing", "enrollment_number": "STU-116"},
    {"phone_number": "19", "email": "student17@example.com", "password": "studentPass123", "full_name": "Ella Young", "course": "Pharmacy", "enrollment_number": "STU-117"},
    {"phone_number": "20", "email": "student18@example.com", "password": "studentPass123", "full_name": "Oliver King", "course": "Music", "enrollment_number": "STU-118"},
    {"phone_number": "21", "email": "student19@example.com", "password": "studentPass123", "full_name": "Sophia Scott", "course": "Theater", "enrollment_number": "STU-119"},
    {"phone_number": "22", "email": "student20@example.com", "password": "studentPass123", "full_name": "Liam Adams", "course": "Architecture", "enrollment_number": "STU-120"}
]

for data in data_list:
    test_student_signup(data)
