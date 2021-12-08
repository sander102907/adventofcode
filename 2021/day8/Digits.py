class Digits:
    def __init__(self):
        self.signal_patterns = [
            'abcefg',   # 0
            'cf',       # 1
            'acdeg',    # 2
            'acdfg',    # 3
            'bcdf',     # 4
            'abdfg',    # 5
            'abdefg',   # 6
            'acf',      # 7
            'abcdefg',  # 8
            'abcdfg',   # 9
        ]

    def get_digit(self, signal_pattern, mapping):
        remapped = ''.join([mapping[l] for l in signal_pattern])
        return self.signal_patterns.index(''.join(sorted(remapped)))