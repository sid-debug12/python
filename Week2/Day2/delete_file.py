from student_loader import load_students
from student_saver import save_students

# Load students
students = load_students("students.txt")

while True:
    name = input("Enter student name to delete (or 'q' to quit): ").strip()

    if name.lower() == "q":
        break

    if name == "":
        print("Name cannot be empty.")
        continue

    if name in students:
        del students[name]
        print("Student deleted.")
    else:
        print("Student not found.")

# Save updated dictionary
save_students("students.txt", students)

# Display remaining students
print("\nCurrent Students:")
for name, score in students.items():
    print(f"{name:<15} {score:>5}")
