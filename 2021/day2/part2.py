def parse_input(file_path):
    with open(file_path) as f:
        return f.read().splitlines()

def solve(inp):
    distance = 0
    depth = 0
    aim = 0

    for m in inp:
        move_size = int(m.split(" ")[-1])
        if "up" in m:
            aim -= move_size
        elif "down" in m:
            aim += move_size
        else:
            depth += aim * move_size 
            distance += move_size

    return distance * depth


if __name__ == "__main__":
    inp = parse_input('input.txt')
    print(solve(inp))