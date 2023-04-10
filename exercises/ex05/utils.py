"""EX05 - `list` Utility Functions."""
__author__ = "730519262"


def only_evens(list: list[int]) -> list[int]:
    """Returns the even numbers within the list."""
    return_list: list[int] = []
    idx: int = 0

    while idx < len(list):
        if list[idx] % 2 == 0:
            return_list.append(list[idx])
        idx += 1
    return return_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Returns list 1 followed by list 2."""
    return_list: list[int] = list_1 + list_2
    return return_list


def sub(list: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns a subset of a list between a specified start and end index."""
    return_list: list[int] = []

    if start_index < 0:
        start_index = 0
    if end_index >= len(list):
        end_index = len(list)
    if len(list) == 0 or start_index >= len(list) or end_index <= 0:
        return return_list
    
    while start_index < end_index:
        return_list.append(list[start_index])
        start_index += 1
    return return_list