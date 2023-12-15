import os

def hash(step: str) -> int:
    value = 0

    for char in step:
        value += ord(char)
        value *= 17
        value %= 256

    return value

def solve(lines: str) -> None:
    steps = lines[0].split(",")
    boxes = [[] for _ in range(256)]

    for step in steps:
        if "=" in step:
            label, focal_length = step.split("=")
            focal_length = int(focal_length)
            box = boxes[hash(label)]

            idxs = [i for i, x in enumerate(box) if x[0] == label]

            if len(idxs) > 0:
                box[idxs[0]] = (label, focal_length)
            else:
                box.append((label, focal_length))

        if "-" in step:
            label = step.split("-")[0]
            box = boxes[hash(label)]

            to_remove_idx = [i for i, x in enumerate(box) if x[0] == label]

            if len(to_remove_idx) > 0:
                box.pop(to_remove_idx[0])

    output = 0

    for i, box in enumerate(boxes):
        for j, item in enumerate(box):
            output += (i + 1) * (j + 1) * item[1]

    print(output)


if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
