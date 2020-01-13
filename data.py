from game import Result
from pathlib import Path
from pickle import dump, load
from player import NUMBER_OF_RESULTS_TO_CONSIDER, Square

DATA_FILE = 'data.pkl'


def print_data(data):
    square_chars = {
        Square.Empty: ' ',
        Square.Mine: 'M',
        Square.Yours: 'Y',
        Square.Considering: '?',
    }

    for position, results in sorted(data.items()):
        if (position.count(Square.Empty) == 8):
            latest_results = results[-NUMBER_OF_RESULTS_TO_CONSIDER:]
            wins = latest_results.count(1)
            losses = latest_results.count(-1)
            draws = latest_results.count(0)

            print(
                [square_chars[square] for square in position],
                (wins, losses, draws)
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
