import os
import re
from typing import List
from dataclasses import dataclass
from functools import cached_property
import numpy as np
from copy import deepcopy


@dataclass
class Row:
    damaged_idxs: List[int]
    unknown_idxs: List[int]
    groups: List[int]
    width: int

    @property
    def num_arrangements(self) -> int:
        arrangement = []
        start_idx = 0

        for group in self.groups:
            arrangement.append(np.array(range(start_idx, start_idx + group)))
            start_idx += group + 1

        return self._slide(arrangement, 0, self._end(arrangement[0][-1], 0))

    def _end(self, start, group_idx):
        return (
            self.width
            - sum(self.groups[group_idx + 1 :])
            - len(self.groups[group_idx + 1 :])
            - start
        )

    @cached_property
    def idxs_set(self):
        return set(self.damaged_idxs + self.unknown_idxs)

    def _slide(self, arrangement, group_idx, end):
        arrangements = 0

        for _ in range(end):
            if group_idx >= len(arrangement) - 1:
                arrangements += 1 if self._check_arrangement(arrangement) else 0

            else:
                arrangements += self._slide(
                    deepcopy(arrangement),
                    group_idx + 1,
                    self._end(arrangement[group_idx + 1][-1], group_idx + 1),
                )

            for idx in range(group_idx, len(arrangement)):
                arrangement[idx] += 1

        return arrangements

    def _check_arrangement(self, arrangement) -> bool:
        return set(self.damaged_idxs) <= set(
            [j for sub in arrangement for j in sub]
        ) and all([set(x) <= self.idxs_set for x in arrangement])


def solve(lines: str) -> None:
    total_arrangements = 0

    for line in lines:
        damaged_idxs = [x.start() for x in re.finditer("#", line)]
        unknown_idxs = [x.start() for x in re.finditer(r"\?", line)]
        groups = [int(x) for x in re.findall(r"\d+", line)]

        row = Row(damaged_idxs, unknown_idxs, groups, len(line.split(" ")[0]))
        total_arrangements += row.num_arrangements

    print(total_arrangements)


if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
