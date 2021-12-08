from Lanternfishes import Lanternfishes

def parse_input(file_path):
    with open(file_path) as f:
        return list(map(int, f.read().split(',')))

def solve(inp):
    lanternfishes = Lanternfishes(inp)

    for day in range(256):
        lanternfishes.new_day()
    
    return lanternfishes.get_total_lanternfishes()

if __name__ == "__main__":
    inp = parse_input('input.txt')
    print(solve(inp))