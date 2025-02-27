from calculator import add

import pytest

def test_empty_string():
    assert add("") == 0 # test case for zerp

def test_string_return_single_number():
    assert add("1") == 1 # test case for single number


def test_two_number_string():
    assert add("1,5") == 6 # test case for two numbers


def test_multiple_number_string():
    assert add("1,5,9") == 15 # test case for multiple numbers

def test_new_lines_as_delimiter():
    assert add("1\n2\n3") == 6 # test case for new line

def test_custom_delimters():
    assert add("//;\n1;2") == 3 # test case for custom delimter

def test_negative_numbers_throw_an_exception():
    with pytest.raises(ValueError,match="negative numbers not allowed -2"):
        add("1,-2") # test case for negative numbers

def test_multi_negative_numbers_show():
    with pytest.raises(ValueError,match="negative numbers not allowed -1, -2"):
        add("-1,-2,3") # test case for multi negative numbers
def test_ignore_if_numbers_a_1000():
    assert add("1,1001") == 1 # test case for ignoring above 1000

# def test_custom_multiple_delimiter():
#     assert add("//[*][%]\n1*2%3") == 6 # test case for multiple delimiter