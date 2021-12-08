def parse_input(file_path):
    with open(file_path) as f:
        return f.read().splitlines()

def solve(inp):
    return sum([1 if int(inp[i]) > int(inp[i - 1]) else 0 for i in range(1, len(inp))])

if __name__ == "__main__":
    inp = parse_input('input.txt')
    print(solve(inp))