def add_student(students):
    """Add a new student to the dictionary."""
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
