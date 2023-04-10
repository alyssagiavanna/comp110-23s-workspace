"""EX07 - Unit Test for Dictionary Functions."""
__author__ = "730519262"

from exercises.ex07.dictionary import invert, count, favorite_color
import pytest


def test_invert_empty() -> None:
    """Tests if dictionary is empty will return an empty dictionary."""
    assert invert({}) == {}


def test_invert_one_element() -> None:
    """Tests if dictionary contains only one key with a cooresponding value, function will return a dictionary containing the inverted values."""
    assert invert({"pb": "j"}) == {"j": "pb"}


def test_invert_key_error() -> None:
    """Tests if dictionary key and value invert has a key error, function will return the error."""
    with pytest.raises(KeyError):
        input_dict: dict[str, str] = {'jack': 'alyssa', 'todd': 'alyssa'}
        invert(input_dict)


def test_count_empty() -> None:
    """Tests if list is empty will return an empty dictionary."""
    assert count({}) == {}


def test_count_one_element() -> None:
    """Tests if list contains only one element,function will return a dictionary with the element as the key and its value as 1."""
    assert count(["comp110"]) == {"comp110": 1}


def test_count_four_identical_elements() -> None:
    """Test of list contains four identical elements, function returns a dictionary with the key as the four elements and its value equal to 4."""
    assert count(["comp110", "comp110", "comp110", "comp110"]) == {"comp110": 4}


def test_favorite_color_empty() -> None:
    """Tests if dictionary is empty will return an empty string."""
    assert favorite_color({}) == ""


def test_favorite_color_identical_values() -> None:
    """Tests if dictionary contains all identical values for each key, function will return that value."""
    assert favorite_color({"Mason": "red", "Greg": "red", "Alyssa": "red", "Sally": "red"}) == "red"


def test_favorite_color_all_different_values() -> None:
    """Tests if dictionary contains all different values for each value, function returns first value in dictionary."""
    assert favorite_color({"Mason": "orange", "Greg": "blue", "Alyssa": "yellow", "Sally": "red"}) == "orange"