"""Module for handling student file operations."""

# Reading a program file
with open("students.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# Reading a program file line by line
with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Writing in program file
with open("students.txt", "w+", encoding="utf-8") as file:
    file.write("Kimi,100\n")
    file.write("Cid,99\n")

# Appending files
with open("students.txt", "a", encoding="utf-8") as file:
    file.write("Charlie,65\n")

# Using with statement to handle files
with open("students.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# Reading data into dictionary


def load_students(filename):
    """Load students from a file and return a dictionary of names and scores."""
    students = {}
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for l in f:
                name, score = l.strip().split(",")
                students[name] = int(score)
    except FileNotFoundError:
        pass

    return students

# Writing dictionary to file


def save_students(filename, students):
    """Save students dictionary to a file."""
    with open(filename, "w", encoding="utf-8") as f:
        for name, score in students.items():
            f.write(f"{name}, {score}\n")
