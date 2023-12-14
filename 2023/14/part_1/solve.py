import os
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Grid:
    r_rocks: List[Tuple[int, int]]
    c_rocks: List[Tuple[int, int]]
    height: int

    @staticmethod
    def from_lines(lines: str):
        r_rocks = []
        c_rocks = []

        for r, line in enumerate(lines):
            for c, char in enumerate(line.strip()):
                if char == "O":
                    r_rocks.append((r, c))
                if char == "#":
                    c_rocks.append((r, c))

        return Grid(r_rocks, c_rocks, len(lines))

    def _rock_rows_in_column_above_row(self, row: int, col: int):
        return sorted(
            [r[0] for r in self.c_rocks if r[1] == col and r[0] < row]
            + [r[0] for r in self.r_rocks if r[1] == col and r[0] < row]
        )

    def tilt_north(self):
        for idx, r_rock in enumerate(self.r_rocks):
            rows = self._rock_rows_in_column_above_row(*r_rock)

            if len(rows) > 0:
                self.r_rocks[idx] = (rows[-1] + 1, r_rock[1])
            else:
                self.r_rocks[idx] = (0, r_rock[1])

    @property
    def score(self):
        return sum([self.height - r[0] for r in self.r_rocks])


def solve(lines: str) -> None:
    grid = Grid.from_lines(lines)
    grid.tilt_north()
    print(grid.score)


if __name__ == "__main__":
    input_file = "sample_input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
