from functions import get_rows
from os import system

CHARS = [' ', 'X', 'O', 'M', 'Y', '?']


def clear():
    system('clear')


def get_char(symbol):
    return CHARS[symbol.value]


def print_board(board):
    rows = ['│'.join([' {0} '.format(get_char(symbol))
                      for symbol in row]) for row in get_rows(board)]

    print('\n───┼───┼───\n'.join(rows))


def print_data(data):
    for key, move_data in sorted(data.items()):
        print([get_char(symbol) for symbol in key], move_data)


def print_percentage(decimal):
    percentage = round(decimal * 100)
    percentage_string = '{0: >4}'.format(str(percentage) + '%')

    print('\n{0}{1}│{2}'.format('─' * percentage,
                                ' ' * (100 - percentage), percentage_string))
