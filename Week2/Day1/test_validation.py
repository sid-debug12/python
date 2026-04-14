import pytest
from module.validation import validate_students


def test_format():

    students = {
        "N": 100,
        "D": 64
    }

    result = validate_students(students)

    assert result == [
        "N   100",
        "D    64"
    ]


def test_empty_dict():
    assert not validate_students({})


def test_invalid_score_type():
    students = {
        "N": "L"
    }
    with pytest.raises(ValueError):
        validate_students(students)


def test_score_out_of_range():
    students = {
        "N": 160
    }
    with pytest.raises(ValueError):
        validate_students(students)


def test_score_sign():
    students = {
        "D": -64
    }
    with pytest.raises(ValueError):
        validate_students(students)
