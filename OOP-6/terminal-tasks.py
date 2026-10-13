"""Solutions for Terminal I/O. Tasks.

Run with arguments:   python slide11_terminal_io.py Python " python " fastapi
Run without:          python slide11_terminal_io.py
"""

import sys


# ---------------------------------------------------------------- Task 1
def echo_arguments():
    """Print every command-line argument with its position."""
    if len(sys.argv) == 1:
        print("No arguments given.")
    for position, argument in enumerate(sys.argv[1:], start=1):
        print(f"{position}: {argument}")


# ---------------------------------------------------------------- Task 2
def even_or_odd():
    """Ask for a number and say whether it is even or odd."""
    number = int(input("Enter a whole number: "))  # input() returns a str
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


# ---------------------------------------------------------------- Task 3
def score_table():
    """Print (name, score) tuples as an aligned table."""
    scores = [("Alice", 88), ("Bob", 100), ("Charlie", 7)]
    print(f"{'Name':<10}|{'Score':>6}")
    print("-" * 17)
    for name, score in scores:
        print(f"{name:<10}|{score:>6}")


# ---------------------------------------------------------- Project step
def get_keywords():
    """Read keywords from the command line, or ask the user for them."""
    if len(sys.argv) > 1:
        raw_keywords = sys.argv[1:]
    else:
        answer = input("Enter keywords separated by commas: ")
        raw_keywords = answer.split(",")

    keywords = []
    seen = set()  # helper set: fast "have I seen this?" check
    for word in raw_keywords:
        clean = word.strip().lower()
        if clean and clean not in seen:  # skip empty strings and duplicates
            keywords.append(clean)       # the list keeps the order
            seen.add(clean)

    if not keywords:
        sys.exit("No keywords given.")
    return keywords


# ------------------------------------------------------------- Try it out
def main():
    print("Task 1")
    echo_arguments()

    print("\nTask 2")
    even_or_odd()

    print("\nTask 3")
    score_table()

    print("\nProject step")
    print(get_keywords())  # ['python', 'fastapi'] for the test command


if __name__ == "__main__":
    main()