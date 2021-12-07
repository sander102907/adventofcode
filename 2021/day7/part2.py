import numpy as np
import sys

def parse_input(file_path):
    with open(file_path) as f:
        return np.array(list(map(int, f.read().split(','))))

def solve(inp):
    min_fuel_cost = sys.maxsize
    for i in range(min(inp), max(inp)):
        distances = np.abs(inp - i)
        fuel_cost = sum((distances ** 2 + distances) / 2)
        if min_fuel_cost > fuel_cost:
            min_fuel_cost = fuel_cost

    return min_fuel_cost

if __name__ == "__main__":
    inp = parse_input('input.txt')
    print(solve(inp))