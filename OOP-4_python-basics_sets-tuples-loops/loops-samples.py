print("--- 1. FOR LOOP & RANGE ---")
for i in range(1, 6, 2):  # Count from 1 to 5 with step 2
    print("Step:", i)

print("\n--- 2. SEQUENCE ITERATION & ENUMERATE ---")
cities = ["Tokyo", "Paris", "Nairobi"]
for rank, city in enumerate(cities, start=1):
    print(f"#{rank}: {city}")

print("\n--- 3. WHILE LOOP WITH BREAK & CONTINUE ---")
energy = 5
while energy > 0:
    energy -= 1
    if energy == 3:
        print("Skipping step at energy level 3...")
        continue  # Skip rest of loop body for this iteration
    if energy == 1:
        print("Energy critical! Halting loop.")
        break     # Exit loop immediately
    print(f"Running... current energy: {energy}")

print("\n--- 4. LOOP ELSE CLAUSE ---")
numbers = [2, 4, 6]
target = 5

for num in numbers:
    if num == target:
        print("Found target!")
        break
else:
    # Runs ONLY if loop completed without hitting a break
    print(f"Target {target} not found in list.")