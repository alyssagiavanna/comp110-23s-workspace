"""EX04 - `list` Utility Functions."""
__author__ = "730519262"


def all(num_list: list[int], one_num: int) -> bool:
    """Returns True if the list of numbers are equal to the one number."""
    idx: int = 0
    check_num: bool = True

    if num_list == []:
        check_num = False

    while idx < len(num_list) and check_num is True:
        if num_list[idx] != one_num:
            check_num = False
        idx += 1
    return check_num


def max(num_list2: list[int]) -> int:
    """Returns the max number."""
    idx: int = 1
    max_num = num_list2[0]

    if len(num_list2) == 0:
        raise ValueError("max() arg is an empty List")

    while idx < len(num_list2):
        if num_list2[idx] > max_num:
            max_num = num_list2[idx]
        idx += 1
    return max_num


def is_equal(num_list3: list[int], num_list4: list[int]) -> bool:
    """Returns True if the lists are identical."""
    idx: int = 0
    check_num: bool = True

    if num_list3 == [] and num_list4 == []:
        check_num = True
        return check_num
    if num_list3 == [] or num_list4 == []:
        check_num = False
    if len(num_list3) != len(num_list4):
        check_num = False

    while idx < len(num_list3) and check_num is True: 
        if num_list3[idx] == num_list4[idx]:
            idx += 1
        else: 
            check_num = False
    return check_num
