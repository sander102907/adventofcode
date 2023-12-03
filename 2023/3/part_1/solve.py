import os
from dataclasses import dataclass
from typing import List
import re


@dataclass
class GridNumber:
    number: int
    indices: List[int]


@dataclass
class Grid:
    grid: List[List[str]]
    gridnumbers: List[GridNumber]

    @staticmethod
    def from_lines(lines: str):
        grid = []
        gridnumbers = []

        for line in lines:
            # Create grid
            grid.append([*line.strip()])

            # Create grid numbers (pair of number and indices in the grid)
            gridnumbers.extend([
                GridNumber(
                    x.group(),
                    list(range(*x.span())),
                )
                for x in re.finditer(r"\d+", line)
            ])

        return Grid(grid, gridnumbers)


def solve(schematic: str) -> None:
    grid = Grid.from_lines(schematic)
    print(grid.gridnumbers)


if __name__ == "__main__":
    input_file = "sample_input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
