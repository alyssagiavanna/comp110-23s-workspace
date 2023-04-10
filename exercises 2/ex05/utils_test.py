"""Unit Tests!"""
__author__ = "730519262"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Tests if list is empty will return an empty list."""
    assert only_evens([]) == []


def test_only_evens_one_element() -> None:
    """Tests if list has one element will return that one element when even."""
    test_list: list[int] = [2]
    assert only_evens(test_list) == [2]


def test_only_evens_odd_numbers() -> None:
    """Tests if list only has odd numbers will return an empty list."""
    test_list: list[int] = [3, 7, 9, 3]
    assert only_evens(test_list) == []


def test_concat_many() -> None:
    """Tests when given two different lists will return those two lists combined."""
    test_list: list[int] = [1, 2, 3]
    test_list2: list[int] = [4, 5, 6]
    assert concat(test_list, test_list2) == [1, 2, 3, 4, 5, 6]


def test_concat_empty() -> None:
    """Tests if given two empty lists will return one empty list."""
    assert concat([], []) == []


def test_concat_one_empty_list() -> None:
    """Tests if given one list and an empty list will return the first list."""
    test_list: list[int] = [6, 7, 9]
    assert concat(test_list, []) == test_list


def test_sub_with_negatives() -> None:
    """Tests if a given negative start index returns the list from the beginning."""
    test_list: list[int] = [1, -2, 1, -5]
    assert sub(test_list, -847, 4) == test_list


def test_sub_same_index() -> None:
    """Tests of given indexes are the same will return one number from list."""
    test_list: list[int] = [11, 3, 54, 12, 98]
    assert sub(test_list, 2, 2) == [54]


def test_sub_zero_for_index() -> None:
    """Tests if given indexes are out of range of list will return an empty list."""
    test_list: list[int] = [6, 4, 4, 4]
    assert sub(test_list, 4, 4) == []