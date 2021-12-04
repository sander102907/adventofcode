from bingoBoard import BingoBoard

with open('input.txt') as f:
    inputs = f.read()

bingo_boards = []
draw_numbers = inputs.split('\n')[0].split(',')

for board_numbers_string in inputs.split('\n\n')[1:]:
    bingo_boards.append(BingoBoard(board_numbers_string))

def get_output():
    for draw_number in draw_numbers:
        for board in bingo_boards:
            if board.new_number(draw_number):
                return board.sum_unmarked_numbers() * int(draw_number)

print(get_output())

