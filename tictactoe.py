from board import Symbol
from data import print_data, read_data, set_data, write_data
from game import Game, get_result
from player import Player

NUMBER_OF_GAMES_TO_PLAY = 10


def print_percentage(decimal):
    percentage = round(decimal * 100)
    percentage_string = '{0: >4}'.format(str(percentage) + '%')

    print('\n{0}{1}│{2}'.format('─' * percentage,
                                ' ' * (100 - percentage), percentage_string))


def main():
    data = read_data()
    results = []  # only used for displaying percentage of draws

    for _ in range(NUMBER_OF_GAMES_TO_PLAY):
        players = {
            Symbol.O: Player(Symbol.O, data),
            Symbol.X: Player(Symbol.X, data),
        }
        game = Game(players)

        results.append(game.winner)

        for player in players:
            result = get_result(player, game.winner)

            for position in players[player].positions:
                set_data(data, position, result)

        print_percentage(results[-100:].count(None) / 100)

    print_data(data)
    write_data(data)


if __name__ == '__main__':
    main()
