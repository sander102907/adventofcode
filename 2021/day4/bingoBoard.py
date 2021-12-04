import math

class BingoBoard:
    def __init__(this, board_string):
        # represent board as a long list of number, from top left to bottom right (going from the first row, to the second etc..)
        this.numbers = board_string.split()
        this.marked = [False] * len(this.numbers)

        this.row_col_len = int(math.sqrt(len(this.numbers)))

    # insert a new number and return whether that results in a win for this board
    def new_number(this, number):
        if number in this.numbers:
            this.marked[this.numbers.index(number)] = True

            return this.__check_win(number)
        
        return False

    # Check if the new number results in a win for this board
    def __check_win(this, number):
        column = this.numbers.index(number) % this.row_col_len
        row = int(math.floor(this.numbers.index(number) / this.row_col_len))

        column_win = all([this.marked[index] for index in this.__column_indices(column)])
        row_win = all([this.marked[index] for index in this.__row_indices(row)])

        return column_win or row_win

    def __column_indices(this, column):
        return [i + column for i in range(len(this.numbers)) if i % this.row_col_len == 0]

    def __row_indices(this, row):
        return list(range(row * this.row_col_len, row * this.row_col_len + this.row_col_len))

    def sum_unmarked_numbers(this):
        sum = 0
        for i in range(len(this.numbers)):
            if not this.marked[i]:
                sum += int(this.numbers[i])
        return sum