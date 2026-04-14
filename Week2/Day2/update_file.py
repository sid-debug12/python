from student_loader import load_students
from student_saver import save_students

# Load students
students = load_students("students.txt")

# Ask for student name
name = input("Enter student name to update: ").strip()

if name in students:

    while True:
        try:
            new_score = int(input("Enter new score: "))

            if 0 <= new_score <= 100:
                students[name] = new_score
                print(f"Updated: {name} -> {new_score}")
                break
            else:
                print("Score must be between 0 and 100.")

        except ValueError:
            print("Invalid score. Enter a number.")

else:
    print("Student not found.")

# Save updated data
save_students("students.txt", students)

# Display students
print("\nCurrent Students:")

for student_name, score in students.items():
    print(f"{student_name:<15} {score:>5}")
