def parse_input(file_path):
    with open(file_path) as f:
        return f.read().splitlines()

def solve(inp):
    measurements = list(map(int, inp))
    output = 0

    for i in range(1, len(measurements) - 2):
        first_group = measurements[i-1] + measurements[i] + measurements[i+1]
        second_group = measurements[i] + measurements[i+1] + measurements[i+2]

        if second_group > first_group:
            output += 1
    
    return output


if __name__ == "__main__":
    inp = parse_input('input.txt')
    print(solve(inp))