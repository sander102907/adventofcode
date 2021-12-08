def parse_input(file_path):
    with open(file_path) as f:
        return [x.split(' | ')[1].split(' ') for x in f.read().splitlines()]

def solve(inp):
    total = 0
    for l in inp:
        for i in l:
            if len(i) in [2, 3, 4, 7]:
                total += 1

    return total
    


if __name__ == "__main__":
    inp = parse_input('input.txt')
    print(solve(inp))