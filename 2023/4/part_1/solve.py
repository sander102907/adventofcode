import os
from dataclasses import dataclass
from typing import List, Tuple
import re

def parse_game(line: str) -> Tuple[List[int], List[int]]:
    game = line.split(": ")[-1]
    winning_numbers, scratched_numbers = game.split(" | ")

    winning_numbers = winning_numbers.strip().replace("  ", " ").split(" ")
    scratched_numbers = scratched_numbers.strip().replace("  ", " ").split(" ")

    winning_numbers = map(int, winning_numbers)
    scratched_numbers = map(int, scratched_numbers)

    return winning_numbers, scratched_numbers


def compute_matches(winning_numbers: List[int], scratched_numbers: List[int]):
    return len(set(winning_numbers) & set(scratched_numbers))


def solve(cards: str) -> None:
    games = map(parse_game, cards)
    matches = map(lambda g: compute_matches(g[0], g[1]), games)

    output = sum([2**(m-1) for m in matches if m > 0])

    print(output)

if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
