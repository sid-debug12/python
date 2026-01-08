"""
Student Registry System with File Storage
Exercises C, D, E + Persistence
"""

import json
import os

FILE_NAME = "students.json"


# ---------------- FILE HANDLING ---------------- #

def load_students():
    """Load students from file."""
    if not os.path.exists(FILE_NAME):
        return {}

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error reading file. Starting with empty registry.")
        return {}


def save_students(students):
    """Save students to file."""
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# ---------------- STUDENT FUNCTIONS ---------------- #

def input_students():
    """Add students to registry."""
    students = load_students()
    size = int(input("Enter the number of students to add: "))

    for _ in range(size):
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
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a number.")

    save_students(students)
    print("Students saved successfully.")
    return students


def display_students(students):
    """Display student table."""
    if not students:
        print("No students in registry.")
        return

    print("\nStudent Registry")
    print(f"{'Name':<15} {'Score':>5}")
    print("-" * 22)
    for name, score in students.items():
        print(f"{name:<15} {score:>5}")


def student_statistics(students):
    """Calculate statistics."""
    scores = list(students.values())

    lowest = min(scores)
    highest = max(scores)
    average = sum(scores) / len(scores)

    return lowest, highest, average


def search_student(students):
    """Search student by name."""
    name = input("Enter student name to search: ").strip()
    for student in students:
        if student.lower() == name.lower():
            print(f"{student} found with score {students[student]}")
            return
    print("Not Found")


def sort_students(students):
    """Sort students."""
    if not students:
        print("No students to sort.")
        return

    print("\n1. Sort by name")
    print("2. Sort by score (highest first)")
    choice = input("Choose option: ")

    if choice == '1':
        sorted_students = dict(sorted(students.items()))
    elif choice == '2':
        sorted_students = dict(
            sorted(students.items(), key=lambda x: x[1], reverse=True)
        )
    else:
        print("Invalid choice.")
        return

    display_students(sorted_students)


# ---------------- MENU ---------------- #

def menu():
    print("\nMENU")
    print("1. Add students")
    print("2. Display students")
    print("3. Statistics")
    print("4. Search student")
    print("5. Sort students")
    print("6. Exit")


def main():
    students = load_students()
    print("Student registry loaded.")

    while True:
        menu()
        choice = input("Choose (1–6): ")

        if choice == '1':
            students = input_students()
        elif choice == '2':
            display_students(students)
        elif choice == '3':
            if students:
                low, high, avg = student_statistics(students)
                print(f"Lowest: {low}")
                print(f"Highest: {high}")
                print(f"Average: {avg:.2f}")
            else:
                print("No students in registry.")
        elif choice == '4':
            search_student(students)
        elif choice == '5':
            sort_students(students)
        elif choice == '6':
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
