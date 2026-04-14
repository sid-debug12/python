def grade_students(students):
    """
    students: dict[str, int | float]

    Returns:
        dict[str, dict[str, int | str]]
    """

    graded = {}

    for name, score in students.items():
        if not isinstance(score, (int, float)):
            raise ValueError("Score must be a number")

        if not (0 <= score <= 100):
            raise ValueError("Score out of range")

        if score >= 80:
            grade = "A"
        elif score >= 70:
            grade = "B"
        elif score >= 60:
            grade = "C"
        elif score >= 50:
            grade = "D"
        else:
            grade = "F"

        graded[name] = {
            "score": score,
            "grade": grade
        }

    return graded
