from __future__ import annotations

import os
from dataclasses import dataclass
import re

@dataclass
class Game:
    id: int
    blue: int
    red: int
    green: int

    @staticmethod
    def from_string(line: str) -> Game:
        colon_index = line.find(':')
        id = int(line[5:colon_index])

        red_idxs = [r.start() for r in re.finditer('red', line)]
        blue_idxs = [r.start() for r in re.finditer('blue', line)]
        green_idxs = [r.start() for r in re.finditer('green', line)]

        red = sum([int(line[0: red_idx - 1].split(" ")[-1]) for red_idx in red_idxs])
        blue = sum([int(line[0: blue_idx - 1].split(" ")[-1]) for blue_idx in blue_idxs])
        green = sum([int(line[0: green_idx - 1].split(" ")[-1]) for green_idx in green_idxs])

        return Game(id, blue, red, green)
    
    @property
    def is_possible(self):
        return self.red <= 12 and self.blue <= 14 and self.green <= 13



def solve(games: str) -> None:
    """
    Print the sum of all of the calibration values
    """

    games = map(Game.from_string, games)
    games = filter(lambda g: g.is_possible, games)

    output = sum(map(lambda g: g.id, games))
    print(output)


if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
