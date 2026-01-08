from module import table, search_student, student_info


def sorted_table(students_table):
    students_table.sort(key=lambda x: x[1].lower())
    return students_table


def menu():
    print("\nMENU")
    print("1. Add student results")
    print("2. Display results table")
    print("3. Search for a student")
    print("4. Exit")


def main():
    students_table = []
    size = names = scores = largest_score = lowest_score = average_score = None

    while True:
        menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            size, names, scores, largest_score, lowest_score, average_score = student_info()
            students_table = table(size, names, scores,
                                   largest_score, lowest_score, average_score)

        elif choice == '2':
            if students_table:
                sorted_students = sorted_table(students_table)
                for row in sorted_students:
                    print(row)
            else:
                print("No data yet.")

        elif choice == '3':
            if students_table:
                search_student(students_table)
            else:
                print("No data yet.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Choose 1–4.")


if __name__ == "__main__":
    main()
