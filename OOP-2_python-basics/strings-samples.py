print("--- 1. BASICS & ESCAPE SEQUENCES ---")
text = "Hello\tWorld!\nLearning \"Python\""
print(text)
print("Length:", len(text))

print("\n--- 2. INDEXING & SLICING ---")
word = "Python"
print("First letter:", word[0])        # 'P'
print("Last letter:", word[-1])        # 'n'
print("Slice [0:4]:", word[0:4])       # 'Pyth'
print("Reverse:", word[::-1])          # 'nohtyP'

print("\n--- 3. F-STRINGS (FORMATTING) ---")
name = "Alex"
score = 94.556
print(f"Player {name.upper()} scored {score:.1f}%")

print("\n--- 4. COMMON STRING METHODS ---")
raw_input = "  alice_smith@example.com  "
clean_email = raw_input.strip().lower()
print("Cleaned email:", clean_email)

phrase = "apples,bananas,cherries"
fruits = phrase.split(",")
print("Split into list:", fruits)
print("Rejoined with hyphen:", "-".join(fruits))

print("Has '.com'?", clean_email.endswith(".com"))
print("Replace domain:", clean_email.replace("example.com", "gmail.com"))