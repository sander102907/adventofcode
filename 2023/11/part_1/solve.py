from __future__ import annotations

import os
from dataclasses import dataclass
import re
import numpy as np
from itertools import combinations


@dataclass
class Grid:
    galaxies: np.ndarray
    width: int

    def __post_init__(self):
        self._expand_cols()

    @staticmethod
    def from_lines(lines: str) -> Grid:
        width = len(lines[0].strip())

        galaxy_coords = []
        # expanded rows
        exp_rows = 0

        for row, line in enumerate(lines):
            galaxy_line_coords = [
                [row + exp_rows, g.start()] for g in re.finditer("#", line)
            ]
            galaxy_coords += galaxy_line_coords

            if len(galaxy_line_coords) == 0:
                exp_rows += 1

        return Grid(np.array(galaxy_coords), width)

    def get_distances_pairs(self):
        distances = []
        for pair in combinations(self.galaxies, 2):
            distances.append(
                abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1])
            )

        return distances

    def _expand_cols(self):
        cols = self.galaxies[:, 1]
        cols_with_galaxies = set(sorted(cols))

        for col in range(self.width, 0, -1):
            if col not in cols_with_galaxies:
                self.galaxies[:, 1][np.where(self.galaxies[:, 1] > col)] += 1


def solve(lines: str) -> None:
    grid = Grid.from_lines(lines)
    output = sum(grid.get_distances_pairs())

    print(output)


if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
