import os
from typing import List

def _build_history(values: List[int]):

    history = [values]

    # Check if any element is not zero
    while any(values):
        differences = []
        for i in range(len(values) -1):
            differences.append(values[i + 1] - values[i])

        history.append(differences)
        values = differences

    return history

def _extrapolate(history: List[List[int]]):

    # Add zero to the last line
    history[-1].append(0)

    # Work back by summing the last value of each row
    for i in range(len(history) - 2, -1, -1):
        a = history[i][-1]
        b = history[i + 1][-1]
        c = a + b
        history[i].append(c)

    return history






def solve(lines: str) -> None:

    answer = 0

    for line in lines:

        # Split and make int
        values = line.strip().split(' ')
        values = [int(x) for x in values]

        # Build history tree
        history = _build_history(values)

        # Extrapolate
        history = _extrapolate(history)

        # Add last value of first row
        answer += history[0][-1]

    print(answer)


if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
