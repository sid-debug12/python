"""Module for filtering students by grade."""
from module.grade import grade_students


def filter_passed_students(students, score=50):
    """Filter students who have passed with a given score threshold.

    Args:
        students: A dictionary mapping student names to grades.
        score: The minimum passing score (default: 50).

    Returns:
        A dictionary of students with grades >= score.
    """
    if isinstance(students, dict):
        passed_students = {name: grade for name,
                           grade in students.items() if grade >= score}
        return passed_students

    return {}
