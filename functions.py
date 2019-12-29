from enums import Result, Symbol


def get_board(board, square, symbol):
    return board[0:square] + (symbol,) + board[square + 1:9]


def get_columns(board):
    return [board[i::3] for i in range(3)]


def get_diagonals(board):
    return [
        board[::4],
        board[2:7:2],
    ]


def get_is_draw(board):
    is_full = get_is_full(board)
    winner = get_winner(board)

    return is_full and not winner


def get_is_full(board):
    return board.count(Symbol.Empty) == 0


def get_normalized_board(board, player):
    return tuple(map(
        lambda square:
            Symbol.Me if square == player
            else Symbol.Opponent if square == get_other_player(player)
            else square,
        board
    ))


def get_position(board, square, player):
    normalized_board = get_normalized_board(board, player)
    position = get_board(normalized_board, square, Symbol.Considering)

    # TODO get all orientations, sort, and return first

    return position


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


def get_rows(board):
    return [board[i * 3:i * 3 + 3] for i in range(3)]


def get_squares(board, symbol):
    return [i for i in range(9) if board[i] == symbol]


def get_winner(board):
    lines = get_columns(board) + get_rows(board) + get_diagonals(board)

    for line in lines:
        if (line.count(Symbol.X) == 3):
            return Symbol.X

        if (line.count(Symbol.O) == 3):
            return Symbol.O

    return None
