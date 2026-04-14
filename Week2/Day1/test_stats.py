"""Unit tests for the compute_statistics function in module.stats."""
from module.stats import compute_statistics
import pytest


def test_valid_statistics():
    students = {
        "Alice": 80,
        "Bob": 100,
        "Charlie": 60
    }

    lowest, highest, average = compute_statistics(students)

    assert lowest == 60
    assert highest == 100
    assert average == 80


def test_empty_students():
    assert not compute_statistics({})


def test_invalid_score_type():
    students = {"Alice": "ninety"}
    with pytest.raises(ValueError):
        compute_statistics(students)


def test_score_out_of_range():
    students = {"Bob": 120}
    with pytest.raises(ValueError):
        compute_statistics(students)
