import os

def solve(lines: str) -> None:
    directions = lines[0].strip()
    mappings = {}

    for line in lines[2:]:
        start, end = line.strip().split(" = ")
        end_l, end_r = end.replace("(", "").replace(")", "").split(", ")
        mappings[start] = (end_l, end_r)

    current_node = "AAA"
    directions_idx = 0

    while current_node != "ZZZ":
        lr = directions[directions_idx % len(directions)]
        current_node = mappings[current_node][0 if lr == "L" else 1]
        directions_idx += 1

    print(directions_idx)
        


if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
