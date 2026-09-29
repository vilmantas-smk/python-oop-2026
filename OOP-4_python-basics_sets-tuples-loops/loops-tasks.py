# Task 1

number = 7

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

# Task 2

expenses = [12.50, 200.00, 45.00, 150.00, 8.99]
total = 0.0

for amount in expenses:
    if amount > 100.00:
        continue  # Skip expensive items
    total += amount

print(f"Filtered subtotal: ${total:.2f}")

# Task 3

correct_pin = "4921"
inputs = ["1111", "2222", "4921"]
attempts = 0

while attempts < 3:
    user_input = inputs[attempts]  # Simulating sequential user entry
    attempts += 1
    
    if user_input == correct_pin:
        print("Access Granted")
        break
else:
    print("Account Locked")

# Task 4

runners = ["Alice", "Bob", "Charlie", "Diana"]

for place, runner in enumerate(runners, start=1):
    print(f"Place {place}: {runner}")

# Task 5

inventory = ["laptop", "mouse", "keyboard", "monitor"]
search_item = "headset"

for item in inventory:
    if item == search_item:
        print("Item available")
        break
else:
    print("Out of stock")