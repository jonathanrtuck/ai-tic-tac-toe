from game import Result
from pathlib import Path
from pickle import dump, load
from player import Square

DATA_FILE = 'data.pkl'


def print_data(data):
    result_chars = {
        Result.Draw: 'D',
        Result.Loss: 'L',
        Result.Win: 'W',
    }
    square_chars = {
        Square.Empty: ' ',
        Square.Mine: 'M',
        Square.Yours: 'Y',
        Square.Considering: '?',
    }

    for position, results in sorted(data.items()):
        print(
            [square_chars[square] for square in position],
            ''.join([result_chars[result] for result in results])
        )


def read_data():
    path = Path(DATA_FILE)

    if path.exists():
        with path.open('br') as file:
            data = load(file)

            return data

    return {}


def set_data(data, position, result):
    '''create/update this position’s results in the data dictionary'''
    data.setdefault(position, []).append(result)


def write_data(data):
    path = Path(DATA_FILE)

    with path.open('bw') as file:
        dump(data, file)
