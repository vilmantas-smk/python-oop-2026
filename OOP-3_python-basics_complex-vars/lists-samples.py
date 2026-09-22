print("--- 1. INDEXING & MUTABILITY ---")
fruits = ["apple", "banana", "cherry"]
fruits[0] = "avocado"  # Lists are mutable
print("Modified list:", fruits)
print("Last element:", fruits[-1])

print("\n--- 2. ADDING & REMOVING ---")
inventory = ["sword", "shield"]
inventory.append("potion")       # Add to end
inventory.insert(1, "map")       # Insert at index 1
print("After additions:", inventory)

used_item = inventory.pop()     # Removes 'potion'
print("Popped item:", used_item)
inventory.remove("shield")      # Removes 'shield'
print("After removal:", inventory)

print("\n--- 3. SORTING & AGGREGATION ---")
scores = [45, 92, 12, 78, 92]
print("Max score:", max(scores))
print("Average score:", sum(scores) / len(scores))
print("Times 92 appears:", scores.count(92))

scores.sort(reverse=True)       # Sort in-place descending
print("Sorted descending:", scores)

print("\n--- 4. ALIASING VS COPYING ---")
original = [1, 2, 3]
alias = original                # Points to SAME list in memory
clone = original.copy()         # Creates an INDEPENDENT copy

original.append(99)
print("Alias reflects change:", alias)
print("Clone remains isolated:", clone)