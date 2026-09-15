# Task 1
raw_username = "   User_123_PRO   "

# Chain methods together
clean_username = raw_username.strip().lower().replace("pro", "guest")

print("Sanitised Username:", clean_username)

# Task 2
encoded_msg = "XzY14321_TAC_DLIW"

# Extract last 8 characters
extracted = encoded_msg[-8:]

# Reverse it
decoded_msg = extracted[::-1]

print("Decoded Secret:", decoded_msg)

# Task 3
first_name = "sarah"
last_name = "connor"
vip_id = 42

full_name = f"{first_name} {last_name}".title()
badge = f"VIP: {full_name} | ID: {vip_id:04d}"

print(badge)

# Task 4
data_row = "laptop,1299.99,3"

# Unpack split elements directly
product, price_str, qty_str = data_row.split(",")

price = float(price_str)
qty = int(qty_str)
total_val = price * qty

print(f"Product: {product} | Total Inventory Value: ${total_val:.2f}")

# Task 5
website = "https://www.python.org"

# 1. Check security prefix
is_secure = website.startswith("https://")

# 2. Extract domain extension
parts = website.split(".")
extension = parts[-1]

print("Is Secure:", is_secure)
print("Domain Extension:", extension)