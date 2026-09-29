print("--- 1. UNIENESS & DEDUPLICATION ---")
raw_tags = ["python", "code", "python", "data", "code"]
unique_tags = set(raw_tags)
print("Original list:", raw_tags)
print("Deduplicated set:", unique_tags)

print("\n--- 2. ADDING & SAFE REMOVAL ---")
skills = {"Python", "SQL"}
skills.add("Git")
skills.update(["Docker", "Bash"])
skills.discard("Java")       # Safe removal (doesn't fail if missing)
print("Updated skills:", skills)

print("\n--- 3. SET MATHEMATICS ---")
dev_a = {"Python", "SQL", "Docker"}
dev_b = {"Python", "JavaScript", "AWS"}

print("Union (|):", dev_a | dev_b)                  # All unique skills
print("Intersection (&):", dev_a & dev_b)          # Common skills
print("Difference (-):", dev_a - dev_b)            # Unique to dev_a
print("Symmetric Diff (^):", dev_a ^ dev_b)        # Unique to either, not both

print("\n--- 4. FAST MEMBERSHIP CHECK ---")
banned_ips = {"192.168.1.1", "10.0.0.5", "172.16.0.1"}
user_ip = "10.0.0.5"
print(f"Is {user_ip} banned?", user_ip in banned_ips)