# Exercise C: Search System in a Student Dictionary
"""Search system in a student dictionary."""

students = {}
size = int(input("Enter the number of students: "))
print("Fill in the students names and scores: ")
for i in range(size):
    """Collecting students' names and scores."""
    while True:
        name = input("Name: ")
        if name == "":
            print("Name cannot be empty.")
        elif name in students:
            print("Student already exists.")
        else:
            break
    while True:
        try:
            score = float(input("Score: "))
            if 0 <= score <= 100:
                students[name] = score
                break
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a number.")

# Search system dictionary
search_name = input("Enter the student name to search: ").strip()
found = False
for student in students:
    """Search for student name"""
    if search_name.lower() == student.lower():
        found = True
        print(f"{student} with score {students[student]}")
        break
if not found:
    print("Not Found")


# TASK:
# Ask user for a student name
# Search in the dictionary
# Print score if found
# Print clear error if not found
# RULE:
# Case-insensitive search
# No crashes allowed
