import os
from math import lcm

def solve(lines: str) -> None:
    directions = lines[0].strip()
    mappings = {}

    for line in lines[2:]:
        start, end = line.strip().split(" = ")
        end_l, end_r = end.replace("(", "").replace(")", "").split(", ")
        mappings[start] = (end_l, end_r)

    current_nodes = [k for k in mappings if k.endswith("A")]
    directions_idx = 0
    turns = []

    for node in current_nodes:
        directions_idx = 0
        while not node.endswith("Z"):
            lr = directions[directions_idx % len(directions)]
            node = mappings[node][0 if lr == "L" else 1]
            directions_idx += 1
        turns.append(directions_idx)

    print(lcm(*turns))



if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
