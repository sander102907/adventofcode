import os
from dataclasses import dataclass
from typing import List, Tuple
from functools import lru_cache


@dataclass
class Grid:
    r_rocks: List[Tuple[int, int]]
    c_rocks: List[Tuple[int, int]]
    height: int
    width: int

    def __hash__(self) -> int:
        return hash((tuple(self.r_rocks), tuple(self.c_rocks)))

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

        return Grid(r_rocks, c_rocks, len(lines), len(lines[0].strip()))

    @lru_cache(maxsize=None)
    def _rock_rows_in_column_above_row(self, row: int, col: int):
        return sorted(
            [r[0] for r in self.c_rocks if r[1] == col and r[0] < row]
            + [r[0] for r in self.r_rocks if r[1] == col and r[0] < row]
        )

    @lru_cache(maxsize=None)
    def _rock_rows_in_column_below_row(self, row: int, col: int):
        return sorted(
            [r[0] for r in self.c_rocks if r[1] == col and r[0] > row]
            + [r[0] for r in self.r_rocks if r[1] == col and r[0] > row],
        )

    @lru_cache(maxsize=None)
    def _rock_cols_in_row_left_of_col(self, row: int, col: int):
        return sorted(
            [r[1] for r in self.c_rocks if r[0] == row and r[1] < col]
            + [r[1] for r in self.r_rocks if r[0] == row and r[1] < col]
        )

    @lru_cache(maxsize=None)
    def _rock_cols_in_row_right_of_col(self, row: int, col: int):
        return sorted(
            [r[1] for r in self.c_rocks if r[0] == row and r[1] > col]
            + [r[1] for r in self.r_rocks if r[0] == row and r[1] > col],
        )

    def tilt_north(self):
        self.r_rocks.sort(key=lambda x: x[0])
        for idx, r_rock in enumerate(self.r_rocks):
            rows = self._rock_rows_in_column_above_row(*r_rock)

            if len(rows) > 0:
                self.r_rocks[idx] = (rows[-1] + 1, r_rock[1])
            else:
                self.r_rocks[idx] = (0, r_rock[1])

    def tilt_south(self):
        self.r_rocks.sort(key=lambda x: x[0], reverse=True)
        for idx, r_rock in enumerate(self.r_rocks):
            rows = self._rock_rows_in_column_below_row(*r_rock)

            if len(rows) > 0:
                self.r_rocks[idx] = (rows[0] - 1, r_rock[1])
            else:
                self.r_rocks[idx] = (self.height - 1, r_rock[1])

    def tilt_east(self):
        self.r_rocks.sort(key=lambda x: x[-1], reverse=True)
        for idx, r_rock in enumerate(self.r_rocks):
            cols = self._rock_cols_in_row_right_of_col(*r_rock)

            if len(cols) > 0:
                self.r_rocks[idx] = (r_rock[0], cols[0] - 1)
            else:
                self.r_rocks[idx] = (r_rock[0], self.width - 1)

    def tilt_west(self):
        self.r_rocks.sort(key=lambda x: x[-1])
        for idx, r_rock in enumerate(self.r_rocks):
            cols = self._rock_cols_in_row_left_of_col(*r_rock)

            if len(cols) > 0:
                self.r_rocks[idx] = (r_rock[0], cols[-1] + 1)
            else:
                self.r_rocks[idx] = (r_rock[0], 0)

    def cycle(self):
        self.tilt_north()
        self.tilt_west()
        self.tilt_south()
        self.tilt_east()

    @property
    def score(self):
        return sum([self.height - r[0] for r in self.r_rocks])


def solve(lines: str) -> None:
    grid = Grid.from_lines(lines)

    scores = []
    possible_outcomes = []

    cycles = 1000000000

    for i in range(cycles):
        grid.cycle()

        score = grid.score

        if score in scores:
            prev = scores.index(score)
            if prev > 0:
                if (cycles - i - 1) % (prev + 1) == 0:
                    if score in possible_outcomes:
                        print(score)
                        break

                    possible_outcomes.append(score)

        scores.insert(0, score)


if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
