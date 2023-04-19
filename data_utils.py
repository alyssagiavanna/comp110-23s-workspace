"""EX08 - Data Wrangling!"""
__author__ = "730519262"



from csv import DictReader

def read_csv_rows(file_input: list[int]) -> list[dict[str, str]]:
    """Read an entire CSV of data into a `list` of rows."""
    
    result: list[dict[str,str]] = []

    file_handle = open(file_input, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close
    return result


def column_values(input_list: list[dict[str, str]], column: str) -> list[str]:
    """Returns a `list[str]` of all values in a single `column` whose name is the second parameter."""
    result: list[str] = []

    for row in input_list:
        if column in row:
            result.append(row[column])

    return result 

def columnar(input_list: list[dict[str, str]]) -> dict[str, str]:
    """Returns a table represented as a list of rows into one represented as a dictionary of columns."""
    result: dict[str, str] = {}

    first_row: dict[str, str] = input_list[0]
    for column in first_row:
        result[column] = column_values(input_list, column)

    return result
        

def head(input_table: dict[str, list[str]], num_row: int) -> dict[str, list[str]]:
    """Returns a new column-based table with only the first `N` (a parameter) rows of data for each column."""
    result: dict[str, list[str]] = {}
    idx: int = 0

    if num_row == 0:
        return result

    if num_row >= len(input_table):
        return input_table
    
    else:
        for column in input_table:
            while idx < len(input_table):
                value_N_list: list[str] = []
                value_N_list.append(input_table[column][idx])
                idx += 1
            result[column] = value_N_list

    return result


def select(table_input: dict[str, list[str]], list_input: list[str]) -> dict[str, list[str]]:
    """Returns a new column-based table with only a specific subset of the original columns."""
    result: dict[list[str]] = {}
    idx: int = 0

    while idx < len(list_input):
        result[list_input[idx]] = table_input[list_input[idx]]
        idx += 1

    return result   



def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Returns a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}

    for key in table1:
        result[key] = table1[key]
    for key in table2:
        if key in result:
            result[key] += table2[key]
        else:
            result[key] = table2[key]

    return result


def count(input_list: list[str]) -> dict[str, int]:
    """Given a `list[str]`, this function will return a `dict[str, int]` where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    idx: int = 0

    for value in input_list:
        if input_list[idx] in result:
            result[value] += 1
        else:
            result[value] = 1
        idx += 1
    
    return result


