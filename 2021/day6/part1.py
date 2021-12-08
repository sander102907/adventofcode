from Lanternfish import Lanternfish

def parse_input(file_path):
    with open(file_path) as f:
        return f.read().split(',')

def solve(inp):
    lanternfishes = []

    for timer in inp:
        lanternfishes.append(Lanternfish(int(timer)))

    for day in range(80):
        new_lanternfishes = []
        for lfish in lanternfishes:
            if lfish.new_day():
                new_lanternfishes.append(Lanternfish())

        lanternfishes.extend(new_lanternfishes)
    
    return len(lanternfishes)



if __name__ == "__main__":
    inp = parse_input('input.txt')
    print(solve(inp))