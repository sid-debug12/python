from student_loader import load_students

students = load_students("students.txt")

while True:
    search_name = input("Enter name to search (or 'q' to quit): ").strip()

    if search_name.lower() == "q":
        break

    if search_name == "":
        print("Name cannot be empty.")
        continue

    # Case-insensitive search
    found = False

    for name, score in students.items():
        if name.lower() == search_name.lower():
            print(f"{name:<15} {score:>5}")
            found = True
            break

    if not found:
        print("Student not found")
