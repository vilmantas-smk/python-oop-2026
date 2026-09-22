# Task 1

backpack = ["water", "snack", "map"]

backpack.append("flashlight")
backpack.insert(0, "compass")
backpack.remove("snack")

print("Final Backpack:", backpack)
print("Item Count:", len(backpack))

# Task 2

scores = [450, 1200, 890, 2100, 610, 1500]

# Sort in-place descending
scores.sort(reverse=True)

# Slice the first 3 elements
podium = scores[:3]

print("Podium Scores:", podium)

# Task 3
grades = [88, 92, 79, 95, 85]

highest = max(grades)
lowest = min(grades)
average = round(sum(grades) / len(grades), 1)

print(f"Highest: {highest} | Lowest: {lowest}")
print(f"Average Grade: {average}")

# Task 4

cart_a = ["apples", "milk"]
cart_b = ["bread", "milk", "eggs"]

cart_a.extend(cart_b)

milk_count = cart_a.count("milk")
bread_index = cart_a.index("bread")

print("Merged Cart:", cart_a)
print("Milk Count:", milk_count)
print("Bread Index:", bread_index)

# Task 5

original_queue = ["Ticket 1", "Ticket 2", "Ticket 3"]

# Create an independent copy
backup_queue = original_queue.copy()

# Remove first item from original
processed = original_queue.pop(0)

print("Original Queue:", original_queue)
print("Backup Queue:", backup_queue)