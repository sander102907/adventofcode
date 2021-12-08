def parse_input(file_path):
    with open(file_path) as f:
        return f.read().splitlines()

def solve(inp):
    distance = 0
    depth = 0

    for m in inp:
        move_size = int(m.split(" ")[-1])
        if "up" in m:
            depth -= move_size
        elif "down" in m:
            depth += move_size
        else:
            distance += move_size

    return distance * depth


if __name__ == "__main__":
    inp = parse_input('input.txt')
    print(solve(inp))


