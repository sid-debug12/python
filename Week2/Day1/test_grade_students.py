import pytest
from module.grade import grade_students


def test_normal_students():
    students = {
        "Alice": 90,
        "Bob": 75
    }

    result = grade_students(students)

    assert result == {
        "Alice": {"score": 90, "grade": "A"},
        "Bob": {"score": 75, "grade": "B"}
    }


def test_empty_students():
    assert grade_students({}) == {}


def test_invalid_score_type():
    students = {"Alice": "A"}
    with pytest.raises(ValueError):
        grade_students(students)


def test_score_out_of_range():
    students = {"Alice": 120}
    with pytest.raises(ValueError):
        grade_students(students)


def test_boundary_scores():
    students = {
        "Alice": 80,
        "Bob": 70,
        "Charlie": 60,
        "David": 50,
        "Eve": 49
    }

    result = grade_students(students)

    assert result == {
        "Alice": {"score": 80, "grade": "A"},
        "Bob": {"score": 70, "grade": "B"},
        "Charlie": {"score": 60, "grade": "C"},
        "David": {"score": 50, "grade": "D"},
        "Eve": {"score": 49, "grade": "F"}
    }
