# Task 1

location = (40.7128, -74.0060, "New York")

latitude, longitude, city_name = location

print(f"{city_name} is located at {latitude}, {longitude}")

# Task 2

first_place = "Runner B"
second_place = "Runner A"

# Single-line tuple swap
first_place, second_place = second_place, first_place

print(f"1st Place: {first_place} | 2nd Place: {second_place}")

# Task 3

config = ("dark_mode", "notifications_on", "vibrate_off")

# Convert to mutable list
config_list = list(config)
config_list[2] = "vibrate_on"

# Convert back to immutable tuple
updated_config = tuple(config_list)

print("Updated Config:", updated_config)

# Task 4

log_data = ("2026-09-15", "CRITICAL", "Database Timeout", "Server 4", "Retry Attempt 3")

date, severity, *details = log_data

print("Severity:", severity)
print("Details List:", details)

# Task 5

game_board = {
    (0, 0): "Home",
    (2, 3): "Gold Mine",
    (5, 5): "Dragon Lair"
}

player_pos = (2, 3)

if player_pos in game_board:
    print(f"You arrived at: {game_board[player_pos]}")
else:
    print("Empty field")