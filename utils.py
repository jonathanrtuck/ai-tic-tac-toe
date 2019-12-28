from constants import EMPTY, ME, O, OPPONENT, X
from enum import Enum


class Result(Enum):
    Win = 1
    Loss = 2
    Draw = 3


def get_columns(squares):
    return [squares[i::3] for i in range(3)]


def get_diagonals(squares):
    return [
        squares[::4],
        squares[2:7:2],
    ]


def get_is_draw(squares):
    is_full = get_is_full(squares)
    winner = get_winner(squares)

    return is_full and not winner


def get_is_full(squares):
    return squares.count(EMPTY) == 0


def get_normalized_squares(squares, player):
    return tuple(map(
        lambda square:
            ME if square == player
            else OPPONENT if square == get_other_player(player)
            else EMPTY,
        squares
    ))


def get_other_player(symbol):
    if (symbol == O):
        return X
    elif (symbol == X):
        return O
    else:
        return None


def get_result(player, winner):
    if (winner == player):
        return Result.Win

    if (winner == get_other_player(player)):
        return Result.Loss

    return Result.Draw


def get_rows(squares):
    return [squares[i * 3:i * 3 + 3] for i in range(3)]


def get_squares(squares, symbol):
    return [i for i in range(9) if squares[i] == symbol]


def get_winner(squares):
    lines = get_columns(squares) + get_rows(squares) + get_diagonals(squares)

    for line in lines:
        if (line.count(X) == 3):
            return X

        if (line.count(O) == 3):
            return O

    return None


def set_squares(squares, square, symbol):
    return squares[0:square] + (symbol,) + squares[square + 1:9]
