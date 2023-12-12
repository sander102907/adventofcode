import os
import re
from itertools import groupby, product
from typing import List
from dataclasses import dataclass
from functools import cached_property
import numpy as np

@dataclass
class Row:
    damaged_idxs: List[int]
    unknown_idxs: List[int]
    groups: List[int]

    @cached_property
    def damaged_groups(self):
        return self._consecutive_groups(self.damaged_idxs)

    @cached_property
    def unknown_groups(self):
        return self._consecutive_groups(self.unknown_idxs)
    
    def num_arrangements(self) -> int:
        total_groups = [(g, 0) for g in self.damaged_groups] + [(g, 1) for g in self.unknown_groups]
        total_groups = sorted(total_groups, key=lambda x: x[0][0])

        num_arrangements = 0

        min_num_unknowns = (len(self.groups) - len(self.damaged_groups))

        unknown_idxs = np.array(self.unknown_idxs)

        for config in product([0, 1], repeat=len(self.unknown_idxs)):
            config = np.array(config)

            if np.sum(config) >= min_num_unknowns:
                if self._check_arrangement(unknown_idxs[config == 1]):
                    num_arrangements += 1

        return num_arrangements


    def _check_arrangement(self, unknown_idxs: List[int]) -> bool:
        arrangement = sorted(self.damaged_idxs + [x for x in unknown_idxs if x != -1])
        found_groups = self._consecutive_groups(arrangement)

        return [len(g) for g in found_groups] == self.groups


    def _consecutive_groups(self, l: List[int]) -> List[List[int]]:
        groups = []
        for _, g in groupby(enumerate(l), lambda ix : ix[0] - ix[1]):
            groups.append(list(map(lambda ix: ix[1], g)))

        return groups


def solve(lines: str) -> None:
    total_arrangements = 0

    for line in lines:
        damaged_idxs = [x.start() for x in re.finditer("#", line)]
        unknown_idxs = [x.start() for x in re.finditer(r"\?", line)]
        groups = [int(x) for x in re.findall(r"\d+", line)]

        row = Row(damaged_idxs, unknown_idxs, groups)
        total_arrangements += row.num_arrangements()

    print(total_arrangements)

if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
