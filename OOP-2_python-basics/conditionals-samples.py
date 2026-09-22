print("--- 1. COMPARISONS & TRUTHINESS ---")
age = 18
print("Is adult?", age >= 18)
print("Empty string truthiness:", bool(""))       # False
print("Non-empty string truthiness:", bool("Hi")) # True

print("\n--- 2. LOGICAL OPERATORS ---")
has_ticket = True
is_vip = False
print("Standard entry:", has_ticket and not is_vip)
print("Any entry access:", has_ticket or is_vip)

print("\n--- 3. IF / ELIF / ELSE CONTROL FLOW ---")
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score {score} gets grade: {grade}")

print("\n--- 4. MEMBERSHIP CHECKING ---")
banned_users = ["admin", "root", "guest"]
username = "admin"

if username in banned_users:
    print(f"Access denied for '{username}'.")
else:
    print("Access granted.")