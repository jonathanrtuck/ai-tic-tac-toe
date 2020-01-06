from board import (get_board, get_flipped_board,
                   get_rotated_board, get_squares, Symbol)
from enum import IntEnum


class Square(IntEnum):
    Empty = 0
    Mine = 1
    Yours = 2
    Considering = 3


class Player:
    def __init__(self, symbol, data):
        self.data = data
        self.positions = []
        self.symbol = symbol

    def get_move(self, board):
        squares = get_squares(board, Symbol.Empty)
        square = squares[0]
        position = get_position(board, square, self.symbol)

        self.positions.append(position)

        return square


def get_normalized_board(board, player):
    '''
    replace X’s and O’s with values representing a first-person perspective, (my squares vs. your squares).
    '''
    return tuple(map(
        lambda square:
            Square.Mine if square == player
            else Square.Yours if square == get_other_player(player)
            else Square.Empty,
        board
    ))


def get_other_player(symbol):
    if (symbol == Symbol.O):
        return Symbol.X

    if (symbol == Symbol.X):
        return Symbol.O

    return None


def get_position(board, square, player):
    '''
    return the first position from a sorted list of all equivelent orientations.
    '''
    normalized_board = get_normalized_board(board, player)
    orientation_functions = [
        get_rotated_board,
        get_rotated_board,
        get_rotated_board,
        get_flipped_board,
        get_rotated_board,
        get_rotated_board,
        get_rotated_board
    ]
    position = get_board(normalized_board, square, Square.Considering)
    positions = [position]

    for orientation_function in orientation_functions:
        position = orientation_function(position)

        positions.append(position)

    return sorted(positions)[0]
