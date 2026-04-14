"""Test module for the format_students function."""
import pytest
from module.format import format_students


def test_normal_students():
    """Test that format_students correctly formats normal student data."""
    students = {
        "Alice": 90,
        "Bob": 75
    }

    result = format_students(students)

    assert result == [
        "Alice           90",
        "Bob             75"
    ]


def test_empty_students():
    """Test that format_students returns an empty list for empty input."""
    assert not format_students({})


def test_invalid_score_type():
    """Test that format_students raises ValueError for non-numeric scores."""
    students = {"Alice": "A"}

    with pytest.raises(ValueError):
        format_students(students)


def test_score_out_of_range():
    """Test that format_students raises ValueError for scores outside valid range."""
    students = {"Alice": 120}

    with pytest.raises(ValueError):
        format_students(students)
