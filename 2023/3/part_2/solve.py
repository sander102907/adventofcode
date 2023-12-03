import os
from dataclasses import dataclass
from typing import List
import re


@dataclass
class GridNumber:
    number: int
    row: int
    columns: List[int]

    def __eq__(self, other):
        if isinstance(other, GridNumber):
            return (
                self.number == other.number
                and self.row == other.row
                and self.columns == other.columns
            )
        return False

    def __hash__(self) -> int:
        return hash((self.number, self.row, tuple(self.columns)))


@dataclass
class GridGear:
    row: int
    column: int


@dataclass
class Grid:
    grid: List[List[str]]
    gridnumbers: List[GridNumber]
    gridgears: List[GridGear]

    @staticmethod
    def from_lines(lines: str):
        grid = []
        gridnumbers = []
        gridgears = []

        for row, line in enumerate(lines):
            # Create grid
            grid.append([*line.strip()])

            # Create grid numbers (pair of number and indices in the grid)
            gridnumbers.extend(
                [
                    GridNumber(
                        int(x.group()),
                        row,
                        list(range(*x.span())),
                    )
                    for x in re.finditer(r"\d+", line)
                ]
            )

            gridgears.extend(
                [
                    GridGear(row, column)
                    for column, char in enumerate(line)
                    if char == "*"
                ]
            )

        return Grid(grid, gridnumbers, gridgears)

    def _get_gridnumber(self, row, column) -> GridNumber:
        for gridnumber in self.gridnumbers:
            if gridnumber.row == row and column in gridnumber.columns:
                return gridnumber
        return None

    def _adjacent_numbers(self, gear: GridGear) -> List[GridNumber]:
        gridnumbers = []

        # Check row before, self, after
        for row in [-1, 0, 1]:
            row_index = gear.row + row

            # Skip when row out of range
            if row_index < 0 or row_index > len(self.grid) - 1:
                continue

            # Check column before, self, after
            for column in [-1, 0, 1]:
                # Skip self
                if row == 0 and column == 0:
                    continue

                # Column to check
                column_index = gear.column + column

                # Skip when column out of range
                if column_index < 0 or column_index > len(self.grid[row_index]) - 1:
                    continue

                character = self.grid[row_index][column_index]
                if character.isdigit():
                    gridnumbers.append(self._get_gridnumber(row_index, column_index))

        return gridnumbers

    @property
    def gear_ratios(self):
        gear_ratios = []

        for gear in self.gridgears:
            numbers = list(set(self._adjacent_numbers(gear)))

            if len(numbers) == 2:
                gear_ratios.append(numbers[0].number * numbers[1].number)

        return gear_ratios


def solve(schematic: str) -> None:
    grid = Grid.from_lines(schematic)

    x = grid.gear_ratios
    print(sum(x))


if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
