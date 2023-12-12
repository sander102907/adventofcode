import os
import re
from functools import lru_cache

@lru_cache(maxsize=None)
def arrangements(line, groups):
    # The needed characters are more than we have left, cannot find an arrangement..
    if sum(groups) > len(line):
        return 0

    # Check if we found an arrangement:
    # Check if line does not contain any '#' anymore when we are out of groups
    if len(groups) == 0:
        return int("#" not in line)

    # Skip if there is a '.'
    if line[0] == ".":
        return arrangements(line[1:], groups)

    # Now we want to either skip or use the '?'
    amt = 0

    # Skip the '?'
    if line[0] == "?":
        amt += arrangements(line[1:], groups)

    # Check for a matching group at the start
    if "." not in line[: groups[0]] and (
        line[groups[0]] != "#" if len(line) > groups[0] else True
    ):
        amt += arrangements(line[groups[0] + 1 :], groups[1:])

    return amt


def solve(lines: str) -> None:
    total_arrangements = 0

    for line in lines:
        f, s = line.split(" ")
        f = ((f + "?") * 5)[:-1]
        s = (s + ",") * 5

        groups = [int(x) for x in re.findall(r"\d+", s)]

        total_arrangements += arrangements(f, tuple(groups))

    print(total_arrangements)


if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
