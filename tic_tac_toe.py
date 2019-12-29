from enums import Result, Symbol
from functions import (get_board, get_is_draw, get_is_full,
                       get_other_player, get_position, get_result, get_squares, get_winner)
from math import sqrt
from output import clear, print_board, print_data, print_percentage
from random import choice

NUMBER_OF_GAMES_TO_PLAY = 500


class Game:
    def __init__(self):
        self.board = tuple([Symbol.Empty for _ in range(9)])
        self.is_draw = False
        self.moves = []
        self.turn = Symbol.X
        self.winner = None

    def play(self, square):
        self.moves.append((self.board, square, self.turn))

        self.board = get_board(self.board, square, self.turn)

        self.is_draw = get_is_draw(self.board)
        self.winner = get_winner(self.board)

        self.turn = get_other_player(self.turn)

    def save(self, data):
        for board, square, player in self.moves:
            position = get_position(board, square, player)
            result = get_result(player, self.winner)

            set_data(data, position, result)


class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def move(self, board, data):
        empty_squares = get_squares(board, Symbol.Empty)
        weights = [get_weight(data, get_position(
            board, square, self.symbol)) for square in empty_squares]
        highest_weight = max(weights)
        highest_weight_empty_squares = [empty_squares[i] for i, weight in enumerate(
            weights) if weight == highest_weight]

        return choice(highest_weight_empty_squares)


def get_weight(data, position):
    (wins, losses, draws) = data.get(position, (0, 0, 0))

    if (wins and not losses and not draws):
        return 100

    if (losses and not wins and not draws):
        return 0

    return ((wins - losses) * 10) + 50


def get_values(symbols):
    return [symbol.value for symbol in symbols]


def set_data(data, position, result):
    (wins, losses, draws) = data.get(position, (0, 0, 0))

    data[position] = (
        wins + 1 if result == Result.Win else wins,
        losses + 1 if result == Result.Loss else losses,
        draws + 1 if result == Result.Draw else draws,
    )


def main():
    data = {}
    results = []  # only used for displaying percentage of draws

    for _ in range(NUMBER_OF_GAMES_TO_PLAY):
        game = Game()
        players = {
            Symbol.O: Player(Symbol.O),
            Symbol.X: Player(Symbol.X),
        }

        while (not game.winner and not game.is_draw):
            square = players[game.turn].move(game.board, data)

            game.play(square)

        results.append(game.winner)
        game.save(data)

        clear()
        print_board(game.board)
        print_percentage(results[-100:].count(None) / 100)

    print_data(data)


if __name__ == '__main__':
    main()
