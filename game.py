from board import (get_board, get_columns, get_diagonals,
                   get_is_full, get_rows, INITIAL_BOARD, print_board, Symbol)
from enum import IntEnum
from player import get_other_player
from os import system


class Result(IntEnum):
    Win = 1
    Loss = -1
    Draw = 0


class Game:
    def __init__(self, players):
        self.board = INITIAL_BOARD
        self.is_draw = False
        self.turn = Symbol.X
        self.winner = None

        while (not self.winner and not self.is_draw):
            square = players[self.turn].get_move(self.board)

            self.play(square)

        system('clear')
        print_board(self.board)

    def play(self, square):
        self.board = get_board(self.board, square, self.turn)

        self.is_draw = get_is_draw(self.board)
        self.winner = get_winner(self.board)

        self.turn = get_other_player(self.turn)


def get_is_draw(board):
    is_full = get_is_full(board)
    winner = get_winner(board)

    return is_full and not winner


def get_result(player, winner):
    if (winner == player):
        return Result.Win

    if (winner == get_other_player(player)):
        return Result.Loss

    return Result.Draw


def get_winner(board):
    lines = get_columns(board) + get_rows(board) + get_diagonals(board)

    for line in lines:
        if (line.count(Symbol.X) == 3):
            return Symbol.X

        if (line.count(Symbol.O) == 3):
            return Symbol.O

    return None
