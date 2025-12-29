# TASK:
# Display students:
# Sorted alphabetically by name
# Then sorted by score (highest first)
# HINT (not solution):
# You cannot sort a dictionary directly.
# Think.

students = {}
size = int(input("Enter the number of students: "))
print("Fill in the students names and scores: ")
for i in range(size):
    while True:
        name = input("Name: ").strip()
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

# Sort by name

sorted_by_name = dict(sorted(students.items()))
print("\nStudents sorted by name:")
for name, score in sorted_by_name.items():
    print(f"{name:<15} {score:>5}")

# Sort by score (highest first)
sorted_by_score = dict(
    sorted(students.items(), key=lambda item: item[1], reverse=True))
# - reverse=True → sorts in descending order (highest score first)
print("\nStudents sorted by score (highest first):")
for name, score in sorted_by_score.items():
    print(f"{name:<15} {score:>5}")
