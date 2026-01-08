def table(size, names, scores, largest_score, lowest_score, average_score):
    print("\nSTUDENT REPORT CARD")
    print(f"{'No':<5}{'Name':<15}{'Score':<10}")
    print("-" * 30)

    for i in range(size):
        print(f"{i + 1:<5}{names[i]:<15}{scores[i]:<10}")

    print("-" * 30)
    print(f"Highest score: {largest_score}")
    print(f"Lowest score: {lowest_score}")
    print(f"Average score: {round(average_score, 2)}")

    students_table = [[i + 1, names[i], scores[i]] for i in range(size)]
    return students_table
