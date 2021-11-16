import pytest

from data_structure.sort.merge.merge import merge_sort


def test_happy_path():
    actual = merge_sort([8,4,23,42,16,15])
    expected = [4,8,15,16,23,42]
    assert actual == expected

def test_empty_array():
    actual = merge_sort([])
    expected = []
    assert actual == expected

def test_one_element():
    actual = merge_sort([3])
    expected = [3]
    assert actual == expected

def test_sorted_arr():
    actual = merge_sort([3,5,7,8,10])
    expected = [3,5,7,8,10]
    assert actual == expected

def test_contains_duplicates_items_arr():
    actual = merge_sort([7,5,7,8,12,5])
    expected = [5,5,7,7,8,12]
    assert actual == expected
