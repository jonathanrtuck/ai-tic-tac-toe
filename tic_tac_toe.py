from enum import IntEnum
from os import system
from pathlib import Path
from pickle import dump, load
from random import choices
from sys import argv


class Result(IntEnum):
    Win = 1
    Loss = -1
    Draw = 0


class Symbol(IntEnum):
    Empty = 0
    X = 1
    O = 2
    Me = 3
    Opponent = 4
    Considering = 5


CHARS = {
    Symbol.Empty: ' ',
    Symbol.X: 'X',
    Symbol.O: 'O',
    Symbol.Me: 'M',
    Symbol.Opponent: 'Y',
    Symbol.Considering: '?',
}
DATA_FILE = 'data.pkl'


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
        squares = get_squares(board, Symbol.Empty)
        weights = [get_weight(data, get_position(
            board, square, self.symbol)) for square in squares]

        return choices(squares, [weight + 100 for weight in weights])[0]


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


def get_is_draw(board):
    is_full = get_is_full(board)
    winner = get_winner(board)

    return is_full and not winner


def get_is_full(board):
    return board.count(Symbol.Empty) == 0


def get_normalized_board(board, player):
    '''
    replace X’s and O’s with symbols representing a first-person perspective, (my squares vs. opponent’s squares).
    '''
    return tuple(map(
        lambda square:
            Symbol.Me if square == player
            else Symbol.Opponent if square == get_other_player(player)
            else square,
        board
    ))


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
    position = get_board(normalized_board, square, Symbol.Considering)
    positions = [position]

    for orientation_function in orientation_functions:
        position = orientation_function(position)

        positions.append(position)

    return sorted(positions)[0]


def get_other_player(symbol):
    if (symbol == Symbol.O):
        return Symbol.X
    elif (symbol == Symbol.X):
        return Symbol.O
    else:
        return None


def get_result(player, winner):
    if (winner == player):
        return Result.Win

    if (winner == get_other_player(player)):
        return Result.Loss

    return Result.Draw


def get_rotated_board(board):
    '''clockwise'''
    return board[6::-3] + board[7::-3] + board[8::-3]


def get_rows(board):
    return [board[i * 3:i * 3 + 3] for i in range(3)]


def get_square_input(options):
    text = input("Enter a square (0–8): ")

    if (text.isdigit()):
        index = int(text)

        if (options.count(index)):
            return index

    return get_square_input(options)


def get_squares(board, symbol):
    return [i for i, square in enumerate(board) if square == symbol]


def get_weight(data, position):
    '''
    '''
    (wins, losses, draws) = data.get(position, (0, 0, 0))

    number_of_results = wins + losses + draws
    number_of_moves_remaining = (position.count(
        Symbol.Empty) // 2) + 1  # including this one
    uncertainty = 100 * number_of_moves_remaining

    if (uncertainty > number_of_results):
        return 50

    positive_feedback = round((wins / number_of_results) * 50)
    negative_feedback = round((losses / number_of_results) * 50)

    return 50 + positive_feedback - negative_feedback


def get_winner(board):
    lines = get_columns(board) + get_rows(board) + get_diagonals(board)

    for line in lines:
        if (line.count(Symbol.X) == 3):
            return Symbol.X

        if (line.count(Symbol.O) == 3):
            return Symbol.O

    return None


def get_char(symbol):
    return CHARS[symbol.value]


def print_board(board):
    rows = ['│'.join([' {0} '.format(get_char(symbol))
                      for symbol in row]) for row in get_rows(board)]

    print('\n───┼───┼───\n'.join(rows))


def print_data(data):
    for position, results in sorted(data.items()):
        if (position.count(Symbol.Empty) == 5):
            print(
                list(map(get_char, position)),
                results,
                get_weight(data, position),
            )

    print(len(data))


def print_percentage(decimal):
    percentage = round(decimal * 100)
    percentage_string = '{0: >4}'.format(str(percentage) + '%')

    print('\n{0}{1}│{2}'.format('─' * percentage,
                                ' ' * (100 - percentage), percentage_string))


def read_data():
    path = Path(DATA_FILE)

    if path.exists():
        with path.open('br') as file:
            data = load(file)

            return data

    return {}


def set_data(data, position, result):
    '''create/update this position’s results in the data dictionary'''
    (wins, losses, draws) = data.get(position, (0, 0, 0))

    data[position] = (
        wins + 1 if result == Result.Win else wins,
        losses + 1 if result == Result.Loss else losses,
        draws + 1 if result == Result.Draw else draws,
    )


def write_data(data):
    path = Path(DATA_FILE)

    with path.open('bw') as file:
        dump(data, file)


def main():
    number_of_games_to_play = int(argv[1]) if len(
        argv) > 1 and argv[1].isdigit() else None
    data = read_data()
    results = []  # only used for displaying percentage of draws

    if (number_of_games_to_play):
        for _ in range(number_of_games_to_play):
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

            system('clear')
            print_board(game.board)
            print_percentage(results[-100:].count(None) / 100)

        print_data(data)
        write_data(data)
    else:
        game = Game()

        while (not game.winner and not game.is_draw):
            squares = get_squares(game.board, Symbol.Empty)
            weights = [get_weight(data, get_position(
                game.board, square, game.turn)) for square in squares]

            system('clear')
            print_board(game.board)
            print('\nweights: ')
            print('\n'.join(['{0}: {1}'.format(squares[i], weight)
                             for i, weight in enumerate(weights)]))

            game.play(get_square_input(squares))

        system('clear')
        print_board(game.board)


if __name__ == '__main__':
    main()
