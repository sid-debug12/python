"""Student Manager application for managing student records and scores."""


from student_saver import save_students
from student_loader import load_students


def menu():
    """Display the main menu options."""
    print("\n========== Student Manager ==========")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Display Students")
    print("6. Exit")


def add_students(students):
    """Add new students to the dictionary."""
    name = input("Enter student name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    if name in students:
        print("Student already exists.")
        return

    try:
        score = int(input("Enter student score: "))
        if 0 <= score <= 100:
            students[name] = score
            print(f"Student {name} added with score {score}.")
        else:
            print("Score must be between 0 and 100.")
    except ValueError:
        print("Invalid score. Enter a number.")


def delete_student(students):
    """Deleting a student from dictionary"""
    name = input("Enter student name to delete: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return

    if name in students:
        del students[name]
        print("Student deleted.")
    else:
        print("Student not found.")


def search_student(students):
    """Searching for students in dictionary"""
    search_name = input("Enter name to search (or 'q' to quit): ").strip()

    if search_name == "":
        print("Name cannot be empty.")
        return
    for name, score in students.items():
        if name.lower() == search_name.lower():
            print(f"{name:<15} {score:>5}")
            return
    print("Student not found")


def update_student(students):
    """Updating a students information"""
    name = input("Enter student name to update: ").strip()

    if name in students:

        while True:
            try:
                new_score = int(input("Enter new score: "))

                if 0 <= new_score <= 100:
                    students[name] = new_score
                    print(f"Updated: {name} -> {new_score}")
                    break
                print("Score must be between 0 and 100.")

            except ValueError:
                print("Invalid score. Enter a number.")

    else:
        print("Student not found.")


def display_students(students):
    """Displaying all results fron the dictionary file"""
    print("\nCurrent Students:")
    if not students:
        print("No students to display")
        return
    for name, score in sorted(students.items()):
        print(f"{name:<15} {score:>5}")


def main():
    """Main program loop."""

    # Load existing students
    students = load_students("students.txt")

    while True:
        menu()
        choice = input("Choose (1-6): ").strip()

        if choice == '1':
            add_students(students)
            save_students("students.txt", students)

        elif choice == '2':
            delete_student(students)
            save_students("students.txt", students)

        elif choice == '3':
            search_student(students)

        elif choice == '4':
            update_student(students)
            save_students("students.txt", students)

        elif choice == '5':
            display_students(students)

        elif choice == '6':
            print("Exiting. Goodbye.")
            break

        else:
            print("Invalid choice. Please enter number between 1 to 6.")


if __name__ == '__main__':
    main()
