def parse_input(file_path):
    with open(file_path) as f:
        return f.read().splitlines()

def solve(inp):
    most_common_binary = ""
    least_common_binary = ""

    for i in range(len(inp[0])):
        ones = sum([int(x[i]) for x in inp])
        
        if ones > (len(inp)/2):
            most_common_binary += "1"
            least_common_binary += "0"
        else:
            most_common_binary += "0"
            least_common_binary += "1"

    return int(most_common_binary, 2) * int(least_common_binary, 2)


if __name__ == "__main__":
    inp = parse_input('input.txt')
    print(solve(inp))





