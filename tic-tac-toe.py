from random import choices
from os import system

DEFAULT_WEIGHT = 50
MAX_WEIGHT = 100
MIN_WEIGHT = 0
NUMBER_OF_GAMES_TO_PLAY = 10000


class Game:
    def __init__(self):
        self.is_draw = False
        self.is_over = False
        self.squares = tuple([' ' for _ in range(9)])
        self.turn = 'x'
        self.winner = None

    def fill_square(self, index):
        self.squares = self.squares[0:index] + \
            (self.turn,) + self.squares[index + 1:9]

        self.is_draw = get_is_draw(self.squares)
        self.is_over = get_is_over(self.squares)
        self.turn = get_other_char(self.turn)
        self.winner = get_winner(self.squares)


class Player:
    def __init__(self, char):
        self.char = char
        self.picked_squares = []

    def pick_square(self, squares, weights):
        normalized_squares = get_normalized_squares(squares, self.char)
        empty_squares = get_squares(normalized_squares, ' ')
        empty_squares_weights = get_weights(normalized_squares, weights)
        square = choices(empty_squares, empty_squares_weights)[0]

        self.picked_squares.append((normalized_squares, square))

        return square

    def update_weights(self, weights, winner):
        modifier = 0

        if (winner == self.char):
            modifier = 1
        elif (winner == get_other_char(self.char)):
            modifier = -1

        update_weights(weights, self.picked_squares, modifier)


def flip_square(square):  # horizontally
    return square + ((square % 3 - 1) * -2)


assert flip_square(0) == 2
assert flip_square(1) == 1
assert flip_square(2) == 0
assert flip_square(3) == 5
assert flip_square(4) == 4
assert flip_square(5) == 3
assert flip_square(6) == 8
assert flip_square(7) == 7
assert flip_square(8) == 6


def flip_squares(squares):  # horizontally
    return squares[2::-1] + squares[5:2:-1] + squares[8:5:-1]


assert flip_squares((0, 1, 2, 3, 4, 5, 6, 7, 8)) == (2, 1, 0, 5, 4, 3, 8, 7, 6)


def get_column(squares, index):
    return squares[index::3]


assert get_column((0, 1, 2, 3, 4, 5, 6, 7, 8), 0) == (0, 3, 6)
assert get_column((0, 1, 2, 3, 4, 5, 6, 7, 8), 1) == (1, 4, 7)
assert get_column((0, 1, 2, 3, 4, 5, 6, 7, 8), 2) == (2, 5, 8)


def get_is_draw(squares):
    is_full = get_is_full(squares)
    is_winner = get_is_winner(squares)

    return is_full and not is_winner


def get_is_full(squares):
    return squares.count(' ') == 0


assert not get_is_full((' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '))
assert not get_is_full(('x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', ' '))
assert get_is_full(('x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x'))


def get_is_over(squares):
    return get_is_full(squares) or get_winner(squares) != None


def get_is_winner(squares):
    return get_winner(squares) != None


def get_normalized_square(square, player):
    if (square == player):
        return 'm'
    elif (square == get_other_char(player)):
        return 'y'
    else:
        return square


def get_normalized_squares(squares, player):
    return [get_normalized_square(square, player) for square in squares]


def get_other_char(char):
    if (char == 'o'):
        return 'x'
    elif (char == 'x'):
        return 'o'
    else:
        return None


def get_row(squares, index):
    offset = index * 3

    return squares[offset:offset + 3]


assert get_row((0, 1, 2, 3, 4, 5, 6, 7, 8), 0) == (0, 1, 2)
assert get_row((0, 1, 2, 3, 4, 5, 6, 7, 8), 1) == (3, 4, 5)
assert get_row((0, 1, 2, 3, 4, 5, 6, 7, 8), 2) == (6, 7, 8)


def get_squares(squares, char):
    return [i for i in range(9) if squares[i] == char]


def get_updated_weight(weight, observations, modifier):
    if (modifier == 0):
        return weight

    neutral_weight = (MAX_WEIGHT - MIN_WEIGHT) / 2
    # closest distance from 0 or 100
    uncertainty = neutral_weight - abs(neutral_weight - weight)
    strength = 1 / ((observations // 9) + 2)

    return weight + (modifier * uncertainty * strength)


def get_weight(weights, normalized_squares, square):
    weight_keys = get_weight_keys(normalized_squares, square)

    for weight_key in weight_keys:
        if (weights.get(weight_key)):
            return weights.get(weight_key)[0]

    return DEFAULT_WEIGHT


def get_weight_key(normalized_squares, square):
    return str(normalized_squares) + str(square)


def get_weight_keys(normalized_squares, square):
    weight_keys = []

    oriented_squares = normalized_squares
    oriented_square = square
    weight_key = get_weight_key(oriented_squares, oriented_square)
    weight_keys.append(weight_key)

    oriented_squares = rotate_squares(oriented_squares)
    oriented_square = rotate_square(oriented_square)
    weight_key = get_weight_key(oriented_squares, oriented_square)
    weight_keys.append(weight_key)

    oriented_squares = rotate_squares(oriented_squares)
    oriented_square = rotate_square(oriented_square)
    weight_key = get_weight_key(oriented_squares, oriented_square)
    weight_keys.append(weight_key)

    oriented_squares = rotate_squares(oriented_squares)
    oriented_square = rotate_square(oriented_square)
    weight_key = get_weight_key(oriented_squares, oriented_square)
    weight_keys.append(weight_key)

    oriented_squares = flip_squares(oriented_squares)
    oriented_square = flip_square(oriented_square)
    weight_key = get_weight_key(oriented_squares, oriented_square)
    weight_keys.append(weight_key)

    oriented_squares = rotate_squares(oriented_squares)
    oriented_square = rotate_square(oriented_square)
    weight_key = get_weight_key(oriented_squares, oriented_square)
    weight_keys.append(weight_key)

    oriented_squares = rotate_squares(oriented_squares)
    oriented_square = rotate_square(oriented_square)
    weight_key = get_weight_key(oriented_squares, oriented_square)
    weight_keys.append(weight_key)

    oriented_squares = rotate_squares(oriented_squares)
    oriented_square = rotate_square(oriented_square)
    weight_key = get_weight_key(oriented_squares, oriented_square)
    weight_keys.append(weight_key)

    return weight_keys


def get_weights(normalized_squares, weights):
    empty_squares = get_squares(normalized_squares, ' ')
    weights = [get_weight(weights, normalized_squares, square)
               for square in empty_squares]

    return weights


def get_winner(squares):
    columns = [get_column(squares, i) for i in range(3)]
    rows = [get_row(squares, i) for i in range(3)]
    diagonals = [
        squares[::4],
        squares[2:7:2],
    ]

    lines = columns + rows + diagonals

    for line in lines:
        if (line.count('x') == 3):
            return 'x'

        if (line.count('o') == 3):
            return 'o'

    return None


assert get_winner((' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')) == None
assert get_winner((' ', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ')) == None
assert get_winner((' ', ' ', ' ', ' ', 'o', 'o', 'o', ' ', ' ')) == None
assert get_winner(('x', 'o', 'o', 'o', 'x', 'x', 'x', 'o', 'o')) == None
assert get_winner(('x', ' ', ' ', 'x', ' ', ' ', 'x', ' ', ' ')) == 'x'
assert get_winner((' ', 'o', ' ', ' ', 'o', ' ', ' ', 'o', ' ')) == 'o'
assert get_winner(('x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ')) == 'x'
assert get_winner((' ', ' ', ' ', 'o', 'o', 'o', ' ', ' ', ' ')) == 'o'
assert get_winner(('x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x')) == 'x'
assert get_winner((' ', ' ', 'o', ' ', 'o', ' ', 'o', ' ', ' ')) == 'o'


def print_percentage(decimal):
    percentage = round(decimal * 100)

    for i in range(100):
        print('─' if i < percentage else ' ', end="")
    print('│', '{0: >4}'.format(str(percentage) + '%'))


def print_squares(squares):
    print('\n')
    print(
        "\n-----------\n".join([' ' + " | ".join(get_row(squares, i)) + ' ' for i in range(3)]))
    print('\n')


def rotate_square(square):  # clockwise
    return ((square * 3 + 2) % 9) - (square // 3)


assert rotate_square(0) == 2
assert rotate_square(1) == 5
assert rotate_square(2) == 8
assert rotate_square(3) == 1
assert rotate_square(4) == 4
assert rotate_square(5) == 7
assert rotate_square(6) == 0
assert rotate_square(7) == 3
assert rotate_square(8) == 6


def rotate_squares(squares):  # clockwise
    return squares[6::-3] + squares[7::-3] + squares[8::-3]


assert rotate_squares((0, 1, 2, 3, 4, 5, 6, 7, 8)
                      ) == (6, 3, 0, 7, 4, 1, 8, 5, 2)


def update_weights(weights, picked_squares, modifier):
    for normalized_squares, square in picked_squares:
        value, observations = (DEFAULT_WEIGHT, 0)
        weight_keys = get_weight_keys(normalized_squares, square)

        for weight_key in weight_keys:
            if (weights.get(weight_key)):
                value, observations = weights.get(weight_key)
                break

        updated_weight = get_updated_weight(value, observations, modifier)

        weights[weight_key] = (updated_weight, observations + 1)


def main():
    results = []
    weights = {}

    for _ in range(NUMBER_OF_GAMES_TO_PLAY):
        game = Game()
        players = {
            'o': Player('o'),
            'x': Player('x'),
        }

        while (not game.is_over):
            square = players[game.turn].pick_square(game.squares, weights)

            game.fill_square(square)

        for char in players:
            players[char].update_weights(weights, game.winner)

        results.append(game.winner)

        system('clear')
        print_squares(game.squares)
        print_percentage(results[-100:].count(None) / 100)

    for squares, weight in sorted(weights.items()):
        print(squares, weight)


if __name__ == "__main__":
    main()
