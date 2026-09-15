import math

# Task 1
friends_str = "4"
slices = 14

friends = int(friends_str)
slices_per_person = slices // friends
leftovers = slices % friends

print("Slices per person:", slices_per_person)
print("Leftovers:", leftovers)

# Task 2
day1 = 8500
day2 = 12400
day3 = 6200

best_day = max(day1, day2, day3)
worst_day = min(day1, day2, day3)

# Parentheses required to add before dividing
average = (day1 + day2 + day3) / 3

print("Highest:", best_day)
print("Lowest:", worst_day)
print("Average:", average)

# Task 3
morning_temp = -4.56
afternoon_temp = 6.21

swing = abs(afternoon_temp - morning_temp)
rounded_swing = round(swing, 1)

print("Temperature swing:", rounded_swing)

# Task 4
player_health = 100

player_health += 20
player_health -= 35
player_health *= 2

print("Final health:", player_health)

# Task 5
import math

area = 18.5
coverage_per_can = 4

# 1. Find the length of one side
side_length = math.sqrt(area)

# 2. Calculate raw cans needed
raw_cans_needed = area / coverage_per_can

# 3. Round up to whole cans
actual_cans_needed = math.ceil(raw_cans_needed)

print("Wall side length:", side_length)
print("Cans of paint to buy:", actual_cans_needed)