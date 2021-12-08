import numpy as np
from Line import Line

# Select only the horizontal and vertical lines from the 
# input and map them to a list of lines: [Line, Line, ...]
def parse_input(file_path):
    with open(file_path) as f:
        inp = f.read().splitlines()
    
    lines = []
    for coords in inp:
        x1, y1 = map(int, coords.split(' -> ')[0].split(','))
        x2, y2 = map(int, coords.split(' -> ')[1].split(','))
        if x1 == x2 or y1 == y2:
            lines.append(Line(x1, y1, x2, y2))
        else:
            lines.append(Line(x1, y1, x2, y2, diagonal=True))

    return lines

def get_max_coords(inp):
    max_x = 0
    max_y = 0

    for line in inp:
        if line.x1 > max_x:
            max_x = line.x1
        
        if line.x2 > max_x:
            max_x = line.x2

        if line.y1 > max_y:
            max_y = line.y1

        if line.y2 > max_y:
            max_y = line.y2

    return max_x, max_y

def fill_diagram(diagram, inp):
    for line in inp:
        order_x = 1 if line.x1 <= line.x2 else -1
        order_y = 1 if line.y1 <= line.y2 else -1

        if not line.diagonal:
            for x in range(line.x1, line.x2 + order_x, order_x):
                for y in range(line.y1, line.y2 + order_y, order_y):
                    diagram[x, y] += 1

        else:
            range_x = range(line.x1, line.x2 + order_x, order_x)
            range_y = range(line.y1, line.y2 + order_y, order_y)
            for x, y in zip(range_x, range_y):
                diagram[x, y] += 1

def solve(inp):
    max_x, max_y = get_max_coords(inp)
    diagram = np.zeros([max_x + 1, max_y + 1])
    fill_diagram(diagram, inp)
    return np.count_nonzero(diagram >= 2)

if __name__ == "__main__":
    inp = parse_input('input.txt')
    print(solve(inp))