"""CQ04 - Dictionary Function Writing"""
__author__ = "730519262"


def zip(str_list: list[str], num_list: list[int]) -> dict[str,int]:
    """Given 2 lists, each cooresponding index is returned as a dictionary"""
    idx: int = 0
    dictionary : dict[str,int] = {}

    if len(str_list) != len(num_list):
        return {}
    if len(str_list) == 0 or len(num_list) == 0:
        return{}

    while idx < len(str_list):
        dictionary[str_list[idx]] = num_list[idx]
        idx += 1
        
    return dictionary



