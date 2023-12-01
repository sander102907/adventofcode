import os
from typing import Union

NUMBER_STRINGS = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
]

def to_string_number(string: Union[str, int]) -> str:
    """Convert the text to a number string

    Args:
        string (Union[str, int]): The string to conver

    Returns:
        str: return the number as a string
    """
    if isinstance(string, int):
        return str(string)
    
    if len(string) == 1:
        return string
    
    return str(NUMBER_STRINGS.index(string))


def find_occurrences(main_string: str, substring: str, lookup_table: dict) -> dict:
    """Find al occurances of a substring and add to a lookup table

    Args:
        main_string (str): The string to search in
        substring (str): The string to find
        lookup_table (dict): The lookup table to fill

    Returns:
        dict: returns the lookup_table with the found strings
    """

    index = -1

    while True:
        # Find next occurrence of substring
        index = main_string.find(substring, index + 1)

        # If no more occurrences, break out of the loop
        if index == -1:
            break

        # Append the index to the list of occurrences
        lookup_table[index] = to_string_number(substring)

    return lookup_table


def build_lookup_table(line: str) -> dict:
    """Function to build a lookup table with the indexes of each found number

    Args:
        line (str): The string to search in

    Returns:
        dict: lookup table with the indexes of each found number
    """

    lookup_table = {}

    for number_s in NUMBER_STRINGS:
        lookup_table = find_occurrences(line, number_s, lookup_table)

    return lookup_table


def solve(calibration_document: str) -> None:
    """
    Print the sum of all of the calibration values
    """
    total = 0

    for s in calibration_document:
        # Build a lookup table to see the indexes of the numbers in the sentence
        lookup_table = build_lookup_table(s)

        # Get the keys of the dictionary
        keys = lookup_table.keys()

        # Get first and last entry only and convert to int
        numbers = int(lookup_table[min(keys)] + lookup_table[max(keys)])

        # Add to sum
        total += numbers
        
    print(total)

if __name__ == "__main__":
    input_file = "../input/sample_input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
