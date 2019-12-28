from os import system
from utils import get_rows


def clear():
    system('clear')


def print_percentage(decimal):
    percentage = round(decimal * 100)

    for i in range(100):
        print('─' if i < percentage else ' ', end="")

    print('│', '{0: >4}'.format(str(percentage) + '%'))


def print_board(squares):
    rows = get_rows(squares)
    lines = [' ' + " | ".join(rows[i]) + ' ' for i in range(3)]

    print('\n')
    print("\n-----------\n".join(lines))
    print('\n')
