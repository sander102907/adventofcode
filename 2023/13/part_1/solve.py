import os
from dataclasses import dataclass
from typing import List


def compute_points(lines: str):
    cols = []

    reflections_h = []
    reflections_v = []

    for i in range(len(lines) - 1):
        if lines[i] == lines[i + 1]:
            reflections_h.append(i)

    for r in range(len(lines[0])):
        col = []
        for line in lines:
            col.append(line[r])
        cols.append(col)

        if r > 0 and col == cols[r - 1]:
            reflections_v.append(r)

    refl = None

    for h_refl in reflections_h:
        r = min(h_refl + 1, len(lines) - h_refl - 1)

        perfect_refl = True

        for back, forward in zip(
            range(h_refl - 1, h_refl - r, -1), range(h_refl + 2, h_refl + r + 1)
        ):
            if lines[back] != lines[forward]:
                perfect_refl = False
                break

        if perfect_refl:
            refl = (h_refl + 1) * 100
            break

    if refl is None:
        for v_refl in reflections_v:
            r = min(v_refl + 1, len(cols) - v_refl + 1)

            perfect_refl = True

            for back, forward in zip(
                range(v_refl - 2, v_refl - r, -1), range(v_refl + 1, v_refl + r + 1)
            ):
                if cols[back] != cols[forward]:
                    perfect_refl = False
                    break

            if perfect_refl:
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
