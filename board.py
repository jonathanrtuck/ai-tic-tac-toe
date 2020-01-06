from enum import IntEnum


class Symbol(IntEnum):
    Empty = 0
    X = 1
    O = 2


INITIAL_BOARD = tuple([Symbol.Empty for _ in range(9)])


def get_board(board, square, symbol):
    return board[0:square] + (symbol,) + board[square + 1:9]


def get_columns(board):
    return [board[i::3] for i in range(3)]


def get_diagonals(board):
    return [
        board[::4],
        board[2:7:2],
    ]


def get_flipped_board(board):
    '''horizontally'''
    return board[2::-1] + board[5:2:-1] + board[8:5:-1]


def get_is_full(board):
    return board.count(Symbol.Empty) == 0


def get_rotated_board(board):
    '''clockwise'''
    return board[6::-3] + board[7::-3] + board[8::-3]


def get_rows(board):
    return [board[i * 3:i * 3 + 3] for i in range(3)]


def get_squares(board, symbol):
    return [i for i, square in enumerate(board) if square == symbol]


def print_board(board):
    chars = {
        Symbol.Empty: ' ',
        Symbol.X: 'X',
        Symbol.O: 'O',
    }
    rows = ['│'.join([' {0} '.format(chars[symbol]) for symbol in row])
            for row in get_rows(board)]

    print('\n───┼───┼───\n'.join(rows))
