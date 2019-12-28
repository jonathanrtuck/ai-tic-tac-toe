from constants import EMPTY, O, X
from math import sqrt
from output import clear, print_percentage, print_board
from random import choice
from utils import get_is_draw, get_is_full, get_normalized_squares, get_other_player, get_result, get_squares, get_winner, Result, set_squares

NUMBER_OF_GAMES_TO_PLAY = 100


class Board:
    def __init__(self):
        self.clear()

        self.is_full = False

    def clear(self):
        self.squares = tuple([EMPTY for _ in range(9)])

    def play(self, player, square):
        self.squares = set_squares(self.squares, square, player)
        self.is_full = get_is_full(self.squares)


class Game:
    def __init__(self, board):
        self.board = board
        self.is_draw = False
        self.is_over = False
        self.moves = []
        self.turn = X
        self.winner = None

    def play(self, square):
        self.moves.append((self.board.squares, square, self.turn))

        self.board.play(self.turn, square)

        self.is_draw = get_is_draw(self.board.squares)
        self.winner = get_winner(self.board.squares)
        self.is_over = self.board.is_full or self.winner

        self.turn = get_other_player(self.turn)

    def save(self, data):
        for squares, square, player in self.moves:
            normalized_squares = get_normalized_squares(squares, player)

            set_data(data, normalized_squares, square,
                     get_result(player, self.winner))


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def move(self, board, data):
        empty_squares = get_squares(board.squares, EMPTY)
        normalized_squares = get_normalized_squares(board.squares, self.symbol)
        weights = [get_weight(data, normalized_squares, square)
                   for square in empty_squares]
        highest_weight = max(weights)
        highest_weight_empty_squares = [empty_squares[i] for i, weight in enumerate(
            weights) if weight == highest_weight]

        return choice(highest_weight_empty_squares)


def get_key(squares, square):
    return str(squares) + str(square)


def get_weight(data, squares, square):
    key = get_key(squares, square)

    (wins, losses, draws) = data.get(key, (0, 0, 0))

    weight = ((wins - losses) * 10) + 50

    return (0 if weight < 0 else 100 if weight > 100 else weight) ** 3


def set_data(data, squares, square, result):
    key = get_key(squares, square)

    (wins, losses, draws) = data.get(key, (0, 0, 0))

    data[key] = (
        wins + 1 if result == Result.Win else wins,
        losses + 1 if result == Result.Loss else losses,
        draws + 1 if result == Result.Draw else draws,
    )


def main():
    data = {}
    results = []  # only used for displaying percentage of draws

    board = Board()

    for _ in range(NUMBER_OF_GAMES_TO_PLAY):
        game = Game(board)
        players = {
            O: Player(O),
            X: Player(X),
        }

        while (not game.is_over):
            square = players[game.turn].move(game.board, data)

            game.play(square)

        results.append(game.winner)

        clear()
        print_board(game.board.squares)
        print_percentage(results[-100:].count(None) / 100)

        game.save(data)
        game.board.clear()

    for key, move_data in sorted(data.items()):
        print(key, move_data)


if __name__ == "__main__":
    main()
