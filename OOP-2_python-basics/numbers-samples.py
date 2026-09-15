import math

print("--- 1. BASIC & ADVANCED MATH ---")
print("Division (/):", 10 / 3)      # Returns float: 3.3333...
print("Floor (//):", 10 // 3)       # Truncates to int: 3
print("Modulo (%):", 10 % 3)        # Remainder: 1
print("Exponent (**):", 2 ** 3)     # 2 to the power of 3: 8

print("\n--- 2. ORDER OF OPERATIONS & ASSIGNMENT ---")
# Without parentheses vs With parentheses
print("No parens:", 10 + 5 * 2)     # 20
print("With parens:", (10 + 5) * 2) # 30

score = 50
score += 10  # Same as score = score + 10
print("Augmented Assignment:", score)

print("\n--- 3. THE FLOATING POINT QUIRK ---")
print("0.1 + 0.2 =", 0.1 + 0.2)     # Outputs 0.30000000000000004

print("\n--- 4. BUILT-IN FUNCTIONS ---")
print("Absolute:", abs(-42))
print("Round standard:", round(3.14159, 2))
print("Highest number:", max(14, 99, 23))
print("Lowest number:", min(14, 99, 23))

print("\n--- 5. THE MATH MODULE ---")
print("Ceiling (always up):", math.ceil(4.1))   # 5
print("Floor (always down):", math.floor(4.9))  # 4
print("Square Root:", math.sqrt(25))            # 5.0