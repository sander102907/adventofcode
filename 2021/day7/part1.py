import numpy as np

def parse_input(file_path):
    with open(file_path) as f:
        return np.array(list(map(int, f.read().split(','))))

def solve(inp):
    median = np.median(inp)
    return sum(np.abs((inp - median)))



if __name__ == "__main__":
    inp = parse_input('input.txt')
    print(solve(inp))