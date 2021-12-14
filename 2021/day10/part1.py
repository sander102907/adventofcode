def parse_input(file_path):
    with open(file_path) as f:
        return f.read().splitlines()

def solve(inp):
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    error_score = 0

    for line in inp:
        heap = ''
        for char in line:
            if char in pairs.keys():
                heap += char
            elif char == pairs[heap[-1]]:
                heap = heap[:-1]
            else:
                error_score += scores[char]
                break

    return error_score

if __name__ == "__main__":
    inp = parse_input('input.txt')
    print(solve(inp))