print("--- 1. CREATION & SAFE ACCESS ---")
user = {"name": "Alex", "role": "Developer", "level": 3}
print("Direct access:", user["name"])
print("Safe access (missing key):", user.get("salary", "Not Disclosed"))

print("\n--- 2. UPDATING & REMOVING ---")
user["level"] = 4                  # Update existing key
user["email"] = "alex@dev.com"     # Add new key
print("Updated user:", user)

removed_role = user.pop("role")    # Remove key and retrieve value
print("Removed role:", removed_role)

print("\n--- 3. ITERATION METHODS ---")
inventory = {"apples": 10, "bananas": 5, "cherries": 20}

print("Iterating over key-value pairs:")
for item, count in inventory.items():
    print(f"- {item.capitalize()}: {count}")

print("\n--- 4. MEMBERSHIP & DICT MERGING ---")
print("Has apples?", "apples" in inventory)

extra_stock = {"dragonfruit": 8, "apples": 15}
merged_inventory = inventory | extra_stock  # Overwrites 'apples' with 15
print("Merged Inventory:", merged_inventory)