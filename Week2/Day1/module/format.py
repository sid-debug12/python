def format_students(students):
    """
    Takes a dictionary of students and scores
    Returns a list of formatted strings
    """
    formatted = []

    for name, score in students.items():
        if not isinstance(score, (int, float)):
            raise ValueError("Score must be a number")

        if not (0 <= score <= 100):
            raise ValueError("Score out of range")

        formatted.append(f"{name:<15} {score:>5}")

    return formatted
