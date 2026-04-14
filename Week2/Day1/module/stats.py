"""Module for computing statistics on student scores."""


def compute_statistics(students):
    """
    students: dict[str, int | float]

    Returns:
        tuple (lowest, highest, average)

    Rules:
    - students must not be empty
    - scores must be numbers
    - scores must be between 0 and 100

    Raise:
    - ValueError for invalid input
    """

    students_list = []

    for name, score in students.items():
        if not isinstance(score, (int, float)):
            raise ValueError("Score must be a number")
        if not (0 <= score <= 100):
            raise ValueError("Score out of range")
        students.append(f"{name:<15} {score:>5}")

    if not students:
        raise ValueError("No students to compute statistics")
    lowest = min(students_list)
    highest = max(students_list)
    average = sum(students_list) / len(students_list)

    return students_list, lowest, highest, average
