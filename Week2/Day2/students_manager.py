from student_loader import load_students
from student_saver import save_students

# Load students
students = load_students("students.txt")

# Add students
while True:
    name = input("Enter student name (or 'q' to quit): ").strip()

    if name.lower() == "q":
        break

    if name == "":
        print("Name cannot be empty.")
        continue

    try:
        score = int(input("Enter score: "))

        if 0 <= score <= 100:
            students[name] = score
        else:
            print("Score must be between 0 and 100.")

    except ValueError:
        print("Invalid score. Enter a number.")

# Save updated data
save_students("students.txt", students)

# Display students
print("\nCurrent Students:")

for name, score in students.items():
    print(f"{name:<15} {score:>5}")
