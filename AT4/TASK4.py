import os

def save_returns(books):
    with open("returns.log", "a", encoding="utf-8") as log:
        for book in books:
            log.write(book + "\n")

def process(day_file):
    try:
        with open(day_file, "r", encoding="utf-8") as f:
            books = f.read().splitlines()

        save_returns(books)

    except FileNotFoundError as e:
        with open("error.log", "a", encoding="utf-8") as log:
            log.write(f"Missing file: {day_file}\n")

    except OSError as e:
        with open("error.log", "a", encoding="utf-8") as log:
            log.write(f"File error: {e}\n")

# Create three daily files
for day in range(1, 4):
    with open(f"day{day}.txt", "w", encoding="utf-8") as f:
        f.write(f"Book returned on day {day}\n")
        f.write(f"Book {day}A\n")

# Clear old log
open("returns.log", "w").close()

# Process three days
process("day1.txt")
process("day2.txt")
process("day3.txt")

# Test missing file
process("missing.txt")

# Display log
print("Return Log:")
with open("returns.log", "r", encoding="utf-8") as f:
    print(f.read())

# Display error log
if os.path.exists("error.log"):
    print("Error Log:")
    with open("error.log", "r", encoding="utf-8") as f:
        print(f.read())
