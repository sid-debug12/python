def student_info():
    names = []
    scores = []

    size = int(input("Enter the number of students: "))

    print("Enter student names:")
    for i in range(size):
        name = input(f"Student {i + 1} name: ")
        names.append(name)

    print("Enter student scores:")
    for i in range(size):
        while True:
            try:
                score = float(input(f"{names[i]}'s score: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a number.")

    largest_score = max(scores)
    lowest_score = min(scores)
    average_score = sum(scores) / len(scores)

    return size, names, scores, largest_score, lowest_score, average_score
