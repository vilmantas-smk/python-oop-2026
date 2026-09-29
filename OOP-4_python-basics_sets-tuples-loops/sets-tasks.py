# Task 1

rsvps = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Diana"]

guest_set = set(rsvps)
guest_count = len(guest_set)
unique_guests = list(guest_set)

print("Unique Guest Count:", guest_count)
print("Unique Guests List:", unique_guests)

# Task 2

members = {"Alex", "Taylor", "Jordan"}

members.add("Morgan")
members.remove("Taylor")
members.discard("Chris")  # Will not raise an error even though "Chris" is absent

print("Current Members:", members)

# Task 3

alice_friends = {"Bob", "Charlie", "David"}
cleo_friends = {"Charlie", "Diana", "Eve", "Bob"}

common_friends = alice_friends & cleo_friends
all_friends = alice_friends | cleo_friends

print("Common Friends:", common_friends)
print("All Unique Friends Combined:", all_friends)

# Task 4

job_requirements = {"Python", "SQL", "Docker", "Linux", "AWS"}
applicant_skills = {"Python", "SQL", "Git"}

missing_skills = job_requirements - applicant_skills

print("Missing Required Skills:", missing_skills)

# Task 5

security_keys = {"KEY_101", "KEY_204", "KEY_509"}
input_key = "KEY_204"

if input_key in security_keys:
    print("Access Granted")
else:
    print("Access Denied")