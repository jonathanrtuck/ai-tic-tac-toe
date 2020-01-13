from board import Symbol
from data import print_data, read_data, set_data, write_data
from game import Game, get_result
from player import Ai, Human
from sys import argv


def print_percentage(decimal):
    percentage = round(decimal * 100)
    percentage_string = '{0: >4}'.format(str(percentage) + '%')

    print('\n{0}{1}│{2}'.format('─' * percentage,
                                ' ' * (100 - percentage), percentage_string))


def main():
    number_of_games_to_play = int(argv[1]) if len(
        argv) > 1 and argv[1].isdigit() else None
    data = read_data()
    results = []  # only used for displaying percentage of draws

    if (number_of_games_to_play):
        for _ in range(number_of_games_to_play):
            players = {
                Symbol.X: Ai(Symbol.X, data),
                Symbol.O: Ai(Symbol.O, data),
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
    else:
        players = {
            Symbol.X: Human(Symbol.X, data),
            Symbol.O: Human(Symbol.O, data),
        }
        game = Game(players)


if __name__ == '__main__':
    main()
