class BasinHelper:
    def __init__(self, inp):
        self.inp = inp

    def find_basins(self):
        self.basins = []
        for r in range(len(self.inp)):
            for c in range(len(self.inp[r])):
                if self.is_basin(r, c):
                    self.basins.append((r, c))

    def is_basin(self, r, c):
        return (r == 0 or self.inp[r][c] < self.inp[r-1][c]) and \
                (c == 0 or self.inp[r][c] < self.inp[r][c-1]) and \
                (r == len(self.inp) - 1 or self.inp[r][c] < self.inp[r+1][c]) and \
                (c == len(self.inp[r]) - 1 or self.inp[r][c] < self.inp[r][c+1])

    def find_size_basin(self, r, c, basin_coords=[]):

        if (r, c) not in basin_coords:
            basin_coords.append((r, c))

        if r > 0 and self.inp[r-1][c] > self.inp[r][c] and self.inp[r-1][c] < 9:
            self.find_size_basin(r - 1, c, basin_coords)
        
        if c > 0 and self.inp[r][c-1] > self.inp[r][c] and self.inp[r][c-1] < 9:
            self.find_size_basin(r, c - 1, basin_coords)
        
        if r < len(self.inp) - 1 and self.inp[r+1][c] > self.inp[r][c] and self.inp[r+1][c] < 9:
            self.find_size_basin(r+1, c, basin_coords)

        if c < len(self.inp[r]) - 1 and self.inp[r][c+1] > self.inp[r][c] and self.inp[r][c+1] < 9:
            self.find_size_basin(r, c+1, basin_coords)

        return len(basin_coords)