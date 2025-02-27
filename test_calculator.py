from calculator import add

import pytest

def test_empty_string():
    assert add("") == 0

def test_string_return_single_number():
    assert add("1") == 1


def test_two_number_string():
    assert add("1,5") == 6


def test_multiple_number_string():
    assert add("1,5,9") == 15

def test_new_lines_as_delimiter():
    assert add("1\n2\n3") == 6

def test_custom_delimters():
    assert add("//;\n1;2") == 3

def test_negative_numbers_throw_an_exception():
    with pytest.raises(ValueError,match="negative numbers not allowed -2"):
        add("1,-2")

def test_multi_negative_numbers_show():
    with pytest.raises(ValueError,match="negative numbers not allowed -1, -2"):
        add("-1,-2,3")
def test_ignore_if_numbers_a_1000():
    assert add("1,1001") == 1