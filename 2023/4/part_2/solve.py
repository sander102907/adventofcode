import os
from dataclasses import dataclass
from typing import List, Tuple
import re

@dataclass
class Card:
    amount: int
    winning_numbers: List[int]
    scratched_numbers: List[int]



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

    d : dict[int, Card] = {}
    
    for index, game in enumerate(games):
        d[index] = Card(1, game[0], game[1])


    for id, card in d.items():
        matches = compute_matches(card.winning_numbers, card.scratched_numbers)

        for i in range(id + 1, id + 1 + matches):
            d[i].amount += card.amount

    output = sum(map(lambda x: x.amount, d.values()))

    print(output)


if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
