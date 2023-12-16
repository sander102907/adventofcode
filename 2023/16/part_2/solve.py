import os
from dataclasses import dataclass
from enum import Enum
from typing import List, Set


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


@dataclass
class EnergizedCell:
    row: int
    column: int
    direction: Direction

    def __eq__(self, other):
        if not isinstance(other, EnergizedCell):
            return False
        return (
            self.row == other.row
            and self.column == other.column
            and self.direction == other.direction
        )

    def __hash__(self):
        return hash((self.row, self.column, self.direction))


@dataclass
class Beam:
    row: int
    column: int
    direction: Direction

    def can_continue(self, grid, energized_cells: Set[EnergizedCell]):
        cell = EnergizedCell(self.row, self.column, self.direction)

        if self.row >= 0 and self.row < len(grid):
            if self.column >= 0 and self.column < len(grid[self.row]):
                # Check if already visited
                if cell in energized_cells:
                    return False
                else:
                    energized_cells.add(cell)

                return True

        return False

    def next(self, grid):
        extra_beams = []
        char = grid[self.row][self.column]
        # print(char)

        if char == ".":
            if self.direction == Direction.RIGHT:
                self.column += 1
            elif self.direction == Direction.LEFT:
                self.column -= 1
            elif self.direction == Direction.DOWN:
                self.row += 1
            elif self.direction == Direction.UP:
                self.row -= 1

        elif char == "/":
            if self.direction == Direction.RIGHT:
                self.row -= 1
                self.direction = Direction.UP
            elif self.direction == Direction.LEFT:
                self.row += 1
                self.direction = Direction.DOWN
            elif self.direction == Direction.DOWN:
                self.column -= 1
                self.direction = Direction.LEFT
            elif self.direction == Direction.UP:
                self.column += 1
                self.direction = Direction.RIGHT

        elif char == "\\":
            if self.direction == Direction.RIGHT:
                self.row += 1
                self.direction = Direction.DOWN
            elif self.direction == Direction.LEFT:
                self.row -= 1
                self.direction = Direction.UP
            elif self.direction == Direction.DOWN:
                self.column += 1
                self.direction = Direction.RIGHT
            elif self.direction == Direction.UP:
                self.column -= 1
                self.direction = Direction.LEFT

        elif char == "-":
            if self.direction == Direction.RIGHT:
                self.column += 1
            elif self.direction == Direction.LEFT:
                self.column -= 1
            elif self.direction == Direction.DOWN:
                extra_beams.append(Beam(self.row, self.column - 1, Direction.LEFT))
                self.column += 1
                self.direction = Direction.RIGHT
            elif self.direction == Direction.UP:
                extra_beams.append(Beam(self.row, self.column + 1, Direction.RIGHT))
                self.column -= 1
                self.direction = Direction.LEFT

        elif char == "|":
            if self.direction == Direction.RIGHT:
                extra_beams.append(Beam(self.row - 1, self.column, Direction.UP))
                self.row += 1
                self.direction = Direction.DOWN
            elif self.direction == Direction.LEFT:
                extra_beams.append(Beam(self.row + 1, self.column, Direction.DOWN))
                self.row -= 1
                self.direction = Direction.UP
            elif self.direction == Direction.DOWN:
                self.row += 1
            elif self.direction == Direction.UP:
                self.row -= 1

        return extra_beams


def solve_beams(grid, energized_cells: Set[EnergizedCell], initial_beam: Beam):
    beams: List[Beam] = []
    beams.append(initial_beam)

    for beam in beams:
        while beam.can_continue(grid, energized_cells):
            extra_beams = beam.next(grid)
            beams.extend(extra_beams)


def solve(lines: str) -> None:
    grid = {}

    for row, line in enumerate(lines):
        grid[row] = {}
        for column, char in enumerate(line.strip()):
            grid[row][column] = char

    highest_value = -1

    # Find energy for all rows in first and last columns
    for row, line in enumerate(lines):
        for column in [0, len(grid[row]) - 1]:
            energized_cells: Set[EnergizedCell] = set()
            initial_beam = Beam(row, column, Direction.RIGHT if column == 0 else Direction.LEFT)

            solve_beams(grid, energized_cells, initial_beam)

            unique_cells = set()
            for cell in energized_cells:
                unique_cells.add((cell.row, cell.column))

            if len(unique_cells) > highest_value:
                highest_value = len(unique_cells)

    # Find energy for all columns in first and last row
    for row in [0, len(grid) - 1]:
        for column, char in enumerate(grid[row]):
            energized_cells: Set[EnergizedCell] = set()
            initial_beam = Beam(row, column, Direction.DOWN if row == 0 else Direction.UP)

            solve_beams(grid, energized_cells, initial_beam)

            unique_cells = set()
            for cell in energized_cells:
                unique_cells.add((cell.row, cell.column))

            if len(unique_cells) > highest_value:
                highest_value = len(unique_cells)

    print(highest_value)


if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
