# Task 1

age = 67

if age < 12:
    price = 8
elif age >= 65:
    price = 10
else:
    price = 15

print(f"Ticket price: ${price}")

# Task 2

username = "alex_dev"
password = "pass123"

# Non-empty strings evaluate to True in Python
if username and len(password) >= 8:
    print("Registration successful")
else:
    print("Invalid registration details")

# Task 3

email_subject = "CLAIM YOUR FREE PRIZE NOW"
clean_subject = email_subject.upper()

if "FREE" in clean_subject or "WIN" in clean_subject:
    print("Warning: Potential Spam!")
else:
    print("Inbox item clear")

# Task 4

gpa = 3.8
attendance_pct = 92

if gpa >= 3.5 and attendance_pct >= 90:
    status = "High Honors"
elif gpa >= 3.0 and attendance_pct >= 80:
    status = "Honors"
else:
    status = "Standard Standing"

print(f"Academic Status: {status}")

# Task 5

year = 2024

# Divisible by 4 AND (not divisible by 100 OR divisible by 400)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")