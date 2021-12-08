from Digits import Digits

def parse_input(file_path):
    with open(file_path) as f:
        inp = f.read().splitlines()
        inp_patterns = [set(x.split(' | ')[0].split(' ')) for x in inp]
        digit_patterns =  [x.split(' | ')[1].split(' ') for x in inp]

        return inp_patterns, digit_patterns
    
def get_digit_mapping(inp_patterns):
    mapping = {}
    # make sets of patterns of 1, 4, 7, 8
    one = {l for l in list(filter(lambda i: len(i) == 2, inp_patterns))[0]}
    four = {l for l in list(filter(lambda i: len(i) == 4, inp_patterns))[0]}
    seven = {l for l in list(filter(lambda i: len(i) == 3, inp_patterns))[0]}
    eight = {l for l in list(filter(lambda i: len(i) == 7, inp_patterns))[0]}

    mapping['a'] = list(seven - one)[0]
    
    # Get all patterns of 0, 6 and 9 (all lenght 6)
    zero_six_nine = [pattern for pattern in list(filter(lambda i: len(i) == 6, inp_patterns))]

    # We can get segment c and f by checking if which of the characters of 1 is not in all the patterns of 0, 6 and 9
    segment_c_f = list(one)
    idx = 1 if segment_c_f[0] in zero_six_nine[0] and segment_c_f[0] in zero_six_nine[1] and segment_c_f[0] in zero_six_nine[2] else 0
    mapping['c'] = segment_c_f[idx]
    mapping['f'] = segment_c_f[1 - idx]

    # We can get segment d and b by checking if which character of 4 that are not in 1 is not in all the patterns of 0, 6 and 9
    segment_d_b = list(four - one)
    idx = 1 if segment_d_b[0] in zero_six_nine[0] and segment_d_b[0] in zero_six_nine[1] and segment_d_b[0] in zero_six_nine[2] else 0
    mapping['d'] = segment_d_b[idx]
    mapping['b'] = segment_d_b[1 - idx]

    # We can get segment e and g by checking the which of the leftover characters of the segments are not in all the patterns of 0, 6 and 9
    segment_e_g = list(eight - set(mapping.values()))
    idx = 1 if segment_e_g[0] in zero_six_nine[0] and segment_e_g[0] in zero_six_nine[1] and segment_e_g[0] in zero_six_nine[2] else 0
    mapping['e'] = segment_e_g[idx]
    mapping['g'] = segment_e_g[1 - idx]

    # reverse the mapping so we can get the original mapping from the mixed up mapping
    return {v: k for k, v in mapping.items()}


def solve(inp_patterns, digit_patterns):
    total = 0

    digits = Digits()
    for in_patterns, out_patterns in zip(inp_patterns, digit_patterns):
        number = ''
        mapping = get_digit_mapping(in_patterns)
        for pattern in out_patterns:
            number += str(digits.get_digit(pattern, mapping))
        total += int(number)

    return total


if __name__ == "__main__":
    inp_patterns, digit_patterns = parse_input('input.txt')
    print(solve(inp_patterns, digit_patterns))