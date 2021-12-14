from BasinHelper import BasinHelper

def parse_input(file_path):
    with open(file_path) as f:
        return [[int(digit) for digit in line] for line in f.read().splitlines()]


def solve(inp):
    basinHelper = BasinHelper(inp)
    basinHelper.find_basins()
    basin_sizes = []

    for basin in basinHelper.basins:
        basin_sizes.append(basinHelper.find_size_basin(basin[0], basin[1], []))

    output = 1

    for basin_size in sorted(basin_sizes)[-3:]:
        output *= basin_size    

    return output

if __name__ == "__main__":
    inp = parse_input('input.txt')
    print(solve(inp))