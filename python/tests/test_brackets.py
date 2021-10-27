import pytest
from code_challenges.brackets.brackets import validate_brackets

def test_one():
    assert validate_brackets('(')==False

def test_two():
    assert validate_brackets('[({\}]')==False


def test_three():
    assert validate_brackets('()[[Extra Characters]]')==True

def test_four():
    assert validate_brackets('Extra Characters')==True
