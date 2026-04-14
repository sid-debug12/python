import pytest
from module import even_odd
# I know you think I wrongly imported even_odd but I want you to know I got a folder for keeping functions separately.
# When I inport from folder module, I can access all functions inside module folder because of __init__.py file.


def test_even():
    assert even_odd(4) == "Even"


def test_odd():
    assert even_odd(7) == "Odd"


def test_invalid_input():
    with pytest.raises(ValueError):
        even_odd("string")


def test_zero():
    assert even_odd(0) == "Even"
