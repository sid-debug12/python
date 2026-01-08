def student_info():
    """
    Collect names and scores of students.
    Returns two lists: names and scores.
    """

    names = []
    scores = []
    size = int(input("Enter the number of students: "))

    print("Fill in the students names:")
    for i in range(size):
        name = input(f"{i + 1}. ")
        names.append(name)

    print("Fill in the students scores:")
    for i in range(size):
        while True:
            try:
                score = float(input(f"{i + 1}. "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100.")
            except (ValueError):
                print("Invalid Input. Enter a number.")

    return names, scores


def statistics(scores):
    """Return the highest, lowest, and average of a list of scores."""

    highest_score = max(scores)
    lowest_score = min(scores)
    average_score = sum(scores) / len(scores)
    return highest_score, lowest_score, average_score


def table(names, scores):
    """
    Generating the table with
    :param names: align names to the left 
    :param scores: align scores to the right
    """
    print("Student Table")
    print(f"{'-'*5}{'-'*15}{'-'*5}")

    print(f"{'No':<5}{'Name':<15}{'Score':>5}")
    for i in range(len(names)):
        print(f"{i + 1:<5}{names[i]:<15}{scores[i]:>5}")


def menu():
    """Display the menu options."""

    print("Menu")
    print("1. Student Information")
    print("2. Display Table")
    print("3. Show statistics")
    print("4. Exit")


def main():
    """"
    Man=in function to run the student statistics and results table program.
    """

    names = []
    scores = []

    while True:
        menu()
        choice = input("Enter option from [1-4]: ")

        if choice == '1':
            names, scores = student_info()
        elif choice == '2':
            table(names, scores)
        elif choice == '3':
            highest_score, lowest_score, average_score = statistics(scores)
            print(f"Highest Score: {highest_score}")
            print(f"Lowest Score: {lowest_score}")
            print(f"Average Score: {round(average_score, 2)}")

        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 4.")


if __name__ == "__main__":
    main()
