# Build a menu with:
# 1. Add students
# 2. Show table
# 3. Show statistics
# 4. Search student
# 5. Sort students
# 6. Exit

def students_info():
    """Collecting students' names and scores."""

    students = {}
    size = int(input("Enter the number of students: "))
    print("Fill in the students names and scores:")

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
    return students


def students_table(students):
    """Table display of students names and scores."""

    print("\nStudent Registry:")
    for name, score in students.items():
        print(f"{name:<15} {score:>5}")


def students_statistics(students):
    """Calculate and return lowest, highest, and average scores."""

    scores_iterator = iter(students.values())
    first_score = next(scores_iterator)
    lowest_score = first_score
    highest_score = first_score
    total_score = first_score
    count = 1

    for score in scores_iterator:
        if score < lowest_score:
            lowest_score = score
        if score > highest_score:
            highest_score = score
        total_score += score
        count += 1
    average_score = total_score / count
    return lowest_score, highest_score, average_score


def search_student(students):
    """Search for a student by name and print their score if found."""

    search_name = input("Enter the student name to search: ").strip()
    found = False
    for student in students:
        if search_name.lower() == student.lower():
            found = True
            print(f"{student} with score {students[student]}")
            break
    if not found:
        print("Not Found")


def sort_students(students):
    """Sort and display students by name and by score."""

    sorted_by_name = dict(sorted(students.items()))
    print("\nStudents sorted by name:")
    for name, score in sorted_by_name.items():
        print(f"{name:<15} {score:>5}")


def display_menu():
    """Display the menu options."""

    print("\nMenu:")
    print("1. Add students")
    print("2. Show table")
    print("3. Show statistics")
    print("4. Search student")
    print("5. Sort students")
    print("6. Exit")


def main():
    """Main function to run the student registry menu system."""

    students = {}
    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")
        if choice == '1':
            students = students_info()
        elif choice == '2':
            students_table(students)
        elif choice == '3':
            if students:
                lowest, highest, average = students_statistics(students)
                print(f"Lowest Score: {lowest}")
                print(f"Highest Score: {highest}")
                print(f"Average Score: {average:.2f}")
            else:
                print("No students in the registry.")
        elif choice == '4':
            search_student(students)
        elif choice == '5':
            sort_students(students)
        elif choice == '6':
            print("Exiting. Goodbbye.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == '__main__':
    main()
