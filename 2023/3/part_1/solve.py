import os
from dataclasses import dataclass
from typing import List
import re


@dataclass
class GridNumber:
    number: int
    row: int
    indices: List[int]


@dataclass
class Grid:
    grid: List[List[str]]
    gridnumbers: List[GridNumber]

    @staticmethod
    def from_lines(lines: str):
        grid = []
        gridnumbers = []

        for i, line in enumerate(lines):
            # Create grid
            grid.append([*line.strip()])

            # Create grid numbers (pair of number and indices in the grid)
            gridnumbers.extend([
                GridNumber(
                    int(x.group()),
                    i,
                    list(range(*x.span())),
                )
                for x in re.finditer(r"\d+", line)
            ])

        return Grid(grid, gridnumbers)

    def _adjacent_to_symbol(self, gridnumber: GridNumber):

        # For each index in the number
        for index in gridnumber.indices:

            # Check row before, self, after
            for row in [-1, 0, 1]:

                row_index = gridnumber.row + row

                # Skip when row out of range
                if row_index < 0 or row_index > len(self.grid) - 1:
                    continue

                # Check column before, self, after
                for column in [-1, 0, 1]:

                    # Skip self
                    if row == 0 and column == 0:
                        continue

                    # Column to check
                    column_index = index + column

                    # Skip when column out of range
                    if column_index < 0 or column_index > len(self.grid[row_index]) - 1:
                        continue

                    character = self.grid[row_index][column_index]
                    if not character.isdigit() and character != '.':
                        return True
                    
        return False

    @property
    def adjacent_numbers(self):

        adjacent_numbers = []

        for gridnumber in self.gridnumbers:
            if self._adjacent_to_symbol(gridnumber):
                adjacent_numbers.append(gridnumber.number)

        return adjacent_numbers


def solve(schematic: str) -> None:
    grid = Grid.from_lines(schematic)
    print(grid)

    x = grid.adjacent_numbers
    print(sum(x))

if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
