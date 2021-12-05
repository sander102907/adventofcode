from bingoBoard import BingoBoard

def parse_input(file_path):
    with open(file_path) as f:
        return f.read()

def play_bingo(bingo_boards, draw_numbers):
    for draw_number in draw_numbers:
        for board in bingo_boards:
            if board.new_number(draw_number):
                return board.sum_unmarked_numbers() * int(draw_number)

def solve(inp):
    bingo_boards = []
    draw_numbers = inp.splitlines()[0].split(',')

    for board_numbers_string in inp.split('\n\n')[1:]:
        bingo_boards.append(BingoBoard(board_numbers_string))

    return play_bingo(bingo_boards, draw_numbers)


if __name__ == "__main__":
    inp = parse_input('input.txt')
    print(solve(inp))

