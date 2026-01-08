# Your program should now:
#     Ask for number of students, names, and scores
#     Validate scores 0–100
#     Store everything in lists
#     Print a formatted table of names and scores
#     Show largest score, lowest score, average score
#     Allow searching a student by name
#     Allow sorting students alphabetically
#     Wrap functionality in functions
#     Provide a simple text-based menu (UI) to choose options


# STEP 1:
# creating a function for students informations, tables, sorting and searching

def student_info():
    names = []
    scores = []
    size = int(input("Enter the number of students: "))
    print("Fill in the students names: ")

    for i in range(size):
        name = input(f"{i + 1}. name: ")
        names.append(name)

    print("Enter the scores: ")
    for i in range(size):
        try:
            while True:
                score = float(input(""))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
        except (ValueError):
            print("Enter score from 0 to 100")

    largest_score = max(scores)
    lowest_score = min(scores)
    average_score = sum(scores) / len(scores)

    return size, names, scores, largest_score, lowest_score, average_score


def table(size, names, scores, largest_score, lowest_score, average_score):

    print("Student Report Card")
    print("Student NumberStudent NameScore")

    for i in range(size):
        print(f"{i + 1}\t     {names[i]}\t     {scores[i]}\t")

    print(f"The highest score: {largest_score}")
    print(f"The lowest score: {lowest_score}")
    print(f"The average score: {round(average_score)}")
    students_table = [[i+1, names[i], scores[i]] for i in range(size)]
    return students_table


def sorted_table(students_table):
    students_table.sort(key=lambda x: (x[1].lower()))
    return students_table


def search_student(students_table):
    search_name = input("Enter the name to search: ").lower()
    found = False
    for row in students_table:
        if row[1].lower() == search_name:
            print(f"Found: Number={row[0]}, Name={row[1]}, Score={row[2]}")
            found = True
            break
    if not found:
        print("Not found")

# STEP 2:
# Creating a menu function to interact with the User


def menu():
    print("Menu")
    print("1. Add Student Report Card Results")
    print("2. Display Table Of Results")
    print("3. Search For Student")
    print("4. Exit")
    return


def main():
    students_table = []
    size = names = scores = largest = lowest = average = None

    while True:
        menu()
        choice = input("Choose an option (1-4): ")
        if choice in {'1', '2', '3', '4'}:
            if choice == '1':
                size = names = scores = largest = lowest = average = student_info()
                students_table = table(
                    size, names, scores, largest, lowest, average)

            elif choice == '2':
                if students_table:
                    sorted_students = sorted_table(students_table)
                    for row in sorted_students:
                        print(row)
                else:
                    print("No data yet. Please add students first.")
            elif choice == '3':
                if students_table:
                    search_student(students_table)
                else:
                    print("No data yet. Please add students info first.")
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid option. Please choose between 1-4.")


if __name__ == '__main__':
    main()
