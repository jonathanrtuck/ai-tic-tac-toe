from board import (get_board, get_flipped_board,
                   get_rotated_board, get_squares, print_board, Symbol)
from enum import IntEnum
from os import system
from random import choice

NUMBER_OF_RESULTS_TO_CONSIDER = 50


class Square(IntEnum):
    Empty = 0
    Mine = 1
    Yours = 2
    Considering = 3


class Ai:
    def __init__(self, symbol, data):
        self.data = data
        self.positions = []
        self.symbol = symbol

    def get_move(self, board):
        squares = get_squares(board, Symbol.Empty)
        weights = [get_weight(get_position(
            board, square, self.symbol), self.data) for square in squares]
        highest_weight = max(weights)
        highest_weight_squres = [squares[i] for i, weight in enumerate(
            weights) if weight == highest_weight]
        picked_square = choice(highest_weight_squres)
        position = get_position(board, picked_square, self.symbol)

        self.positions.append(position)

        return picked_square


class Human:
    def __init__(self, symbol, data):
        self.data = data
        self.symbol = symbol

    def get_move(self, board):
        system('clear')
        print_board(board)

        squares = get_squares(board, Symbol.Empty)
        weights = [get_weight(get_position(
            board, square, self.symbol), self.data) for square in squares]

        print('weights: ', weights)

        return self.get_square_input(squares)

    def get_square_input(self, options):
        '''recursive'''
        symbol_chars = {
            Symbol.X: 'X',
            Symbol.O: 'O',
        }
        text = input('Enter a square for {0} (0–8): '.format(
            symbol_chars[self.symbol]))

        if (text.isdigit()):
            index = int(text)

            if (options.count(index)):
                return index

        return self.get_square_input(options)


def get_normalized_board(board, player):
    '''replace X’s and O’s with values representing a first-person perspective, (my squares vs. your squares).'''
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
    '''return the first position from a sorted list of all equivelent orientations.'''
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


def get_weight(position, data):
    results = data.get(position, [])

    if (len(results) < NUMBER_OF_RESULTS_TO_CONSIDER):
        return 50

    results_to_consider = results[-NUMBER_OF_RESULTS_TO_CONSIDER:]
    latest_results_total = sum(results_to_consider)
    results_weight = latest_results_total * \
        (50 / NUMBER_OF_RESULTS_TO_CONSIDER)
    weight = 50 + results_weight

    return weight
