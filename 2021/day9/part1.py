def parse_input(file_path):
    with open(file_path) as f:
        return [[int(digit) for digit in line] for line in f.read().splitlines()]

def solve(inp):
    total = 0

    for r in range(len(inp)):
        for c in range(len(inp[r])):
            if (r == 0 or inp[r][c] < inp[r-1][c]) and \
               (c == 0 or inp[r][c] < inp[r][c-1]) and \
               (r == len(inp) - 1 or inp[r][c] < inp[r+1][c]) and \
               (c == len(inp[r]) - 1 or inp[r][c] < inp[r][c+1]):
                total += inp[r][c] + 1
    return total
    

if __name__ == "__main__":
    inp = parse_input('input.txt')
    print(solve(inp))