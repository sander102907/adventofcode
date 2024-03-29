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

    output = sum([hash(step) for step in steps])

    print(output)

if __name__ == "__main__":
    input_file = "input.txt"

    path = os.path.join(os.path.abspath(__file__), "..", "..", "input", input_file)
    with open(path, "r", encoding="utf-8") as f:
        inp = f.readlines()

    solve(inp)
