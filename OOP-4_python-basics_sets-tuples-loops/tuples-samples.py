print("--- 1. CREATION & IMMUTABILITY ---")
point = (10, 20)
single_item = (42,)  # Note trailing comma
print("Tuple type:", type(single_item))

# point[0] = 15  # Uncommenting this throws TypeError: 'tuple' object does not support item assignment

print("\n--- 2. TUPLE UNPACKING ---")
coordinates = (37.7749, -122.4194)
lat, lon = coordinates
print(f"Latitude: {lat}, Longitude: {lon}")

# Extended unpacking with wildcard *
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Variable Swap
a, b = "Left", "Right"
a, b = b, a
print(f"Swapped: a={a}, b={b}")

print("\n--- 3. METHODS & TUPLES AS DICT KEYS ---")
data = ("A", "B", "A", "C", "A")
print("Count of 'A':", data.count("A"))
print("Index of 'B':", data.index("B"))

# Tuples can serve as immutable coordinate keys in dictionaries
grid_map = {
    (0, 0): "Start",
    (0, 1): "Treasure",
    (1, 0): "Trap"
}
print("Location at (0, 1):", grid_map[(0, 1)])