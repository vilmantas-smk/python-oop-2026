# Task 1

player = {
    "username": "Shadow",
    "score": 1500,
    "level": 12
}

guild = player.get("guild", "No Guild")
player["rank"] = "Gold"
player["score"] = 1750

print("Guild:", guild)
print("Updated Profile:", player)

# Task 2

prices = {"laptop": 999.99, "mouse": 25.00, "monitor": 200.00, "cable": 8.50}

for item, price in prices.items():
    if price > 50.00:
        print(f"{item} costs ${price:.2f}")

# Task 3

fruit_basket = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = {}

for fruit in fruit_basket:
    counts[fruit] = counts.get(fruit, 0) + 1

print("Fruit Frequencies:", counts)

# Task 4

company = {
    "engineering": {"head": "Sarah", "budget": 120000},
    "marketing": {"head": "Dave", "budget": 85000}
}

eng_budget = company["engineering"]["budget"]
company["marketing"]["head"] = "Elena"
company["engineering"]["team_size"] = 8

print("Engineering Budget:", eng_budget)
print("Updated Directory:", company)

# Task 5

base_menu = {"burger": 10, "fries": 4, "soda": 2}
seasonal_menu = {"shake": 5, "burger": 12}

base_menu.update(seasonal_menu)
soda_price = base_menu.pop("soda")

print(f"Removed soda (Price: ${soda_price})")
print("Final Menu:", base_menu)