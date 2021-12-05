import math

class BingoBoard:
    def __init__(self, board_string):
        # represent board as a long list of number, from top left to bottom right (going from the first row, to the second etc..)
        self.numbers = board_string.split()
        self.marked = [False] * len(self.numbers)

        self.row_col_len = int(math.sqrt(len(self.numbers)))

    # insert a new number and return whether that results in a win for this board
    def new_number(self, number):
        if number in self.numbers:
            self.marked[self.numbers.index(number)] = True

            return self.__check_win(number)
        
        return False

    # Check if the new number results in a win for this board
    def __check_win(self, number):
        column = self.numbers.index(number) % self.row_col_len
        row = int(math.floor(self.numbers.index(number) / self.row_col_len))

        column_win = all([self.marked[index] for index in self.__column_indices(column)])
        row_win = all([self.marked[index] for index in self.__row_indices(row)])

        return column_win or row_win

    def __column_indices(self, column):
        return [i + column for i in range(len(self.numbers)) if i % self.row_col_len == 0]

    def __row_indices(self, row):
        return list(range(row * self.row_col_len, row * self.row_col_len + self.row_col_len))

    def sum_unmarked_numbers(self):
        sum = 0
        for i in range(len(self.numbers)):
            if not self.marked[i]:
                sum += int(self.numbers[i])
        return sum