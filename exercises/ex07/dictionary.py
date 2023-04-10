"""EX07 - Dictionary Functions."""
__author__ = "730519262"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """The given input dictionary will be returned with the keys and values inverted."""
    new_dict: dict[str, str] = {}

    for key in input_dict:
        val = input_dict[key]
        if val in new_dict:
            raise KeyError("Key Error! You have multiple of the same key.")
        new_dict[val] = key

    return new_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Returns the most popular color value among each of the keys in the dictionary."""
    new_dict: dict[str, int] = {}

    for key in input_dict:
        color = input_dict[key]
        if color not in new_dict:
            new_dict[color] = 1
        else:
            new_dict[color] += 1
    
    favorite: str = ""
    highest_votes: int = 0

    for color in new_dict:
        val: int = new_dict[color]
        if val > highest_votes:
            highest_votes = val
            favorite = color
    
    return favorite


def count(input_list: list[str]) -> dict[str, int]:
    """The given list will be converted into a dictionary where each unique index in list will serve as the keys and the number of times each unique index appears serve as the value."""
    new_dict: dict[str, int] = {}

    for item in input_list:
        if item not in new_dict:
            new_dict[item] = 1
        else:
            new_dict[item] += 1

    return new_dict