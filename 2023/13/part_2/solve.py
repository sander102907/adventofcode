import os
from dataclasses import dataclass
from typing import List

def num_diff(line_1: str, line_2: str):
    return sum(1 for a, b in zip(line_1, line_2) if a != b)

def compute_points(lines: List[str]):
    cols = []

    reflections_h = []
    reflections_v = []

    for i in range(len(lines) - 1):
        diff = num_diff(lines[i], lines[i + 1])
        if diff <= 1:
            reflections_h.append((i, diff == 1))

    for r in range(len(lines[0])):
        col = []
        for line in lines:
            col.append(line[r])
        cols.append(col)

        diff = num_diff(col, cols[r - 1])

        if r > 0 and diff <= 1:
            reflections_v.append((r, diff == 1))

    refl = None

    for h_refl, smudge_fixed in reflections_h:
        r = min(h_refl + 1, len(lines) - h_refl - 1)

        perfect_refl = True

        for back, forward in zip(
            range(h_refl - 1, h_refl - r, -1), range(h_refl + 2, h_refl + r + 1)
        ):
            diff = num_diff(lines[back], lines[forward])
            if diff > 1 or (diff == 1 and smudge_fixed):
                perfect_refl = False
                break

            if diff == 1:
                smudge_fixed = True

        if perfect_refl and smudge_fixed:
            refl = (h_refl + 1) * 100
            break

    if refl is None:
        for v_refl, smudge_fixed in reflections_v:
            r = min(v_refl + 1, len(cols) - v_refl + 1)

            perfect_refl = True

            for back, forward in zip(
                range(v_refl - 2, v_refl - r, -1), range(v_refl + 1, v_refl + r + 1)
            ):
                diff = num_diff(cols[back], cols[forward])
                if diff > 1 or (diff == 1 and smudge_fixed):                       
                    perfect_refl = False
                    break

                if diff == 1:
                    smudge_fixed = True


            if perfect_refl and smudge_fixed:
                refl = v_refl
                break

    return refl


def solve(lines: str) -> None:
    patterns_lines = []
    pattern = []

    for line in lines:
        if len(line.strip()) == 0:
            patterns_lines.append(pattern)
            pattern = []
        else:
            pattern.append(line.strip())

    patterns_lines.append(pattern)

    output = 0

    for pattern in patterns_lines:
        output += compute_points(pattern)

    print(output)


if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
