from board import (get_board, get_columns, get_diagonals, get_flipped_board,
                   get_is_full, get_rotated_board, get_rows, get_squares, Symbol)

_ = Symbol.Empty
X = Symbol.X
O = Symbol.O


assert get_board(board=(_, _, _, _, _, _, _, _, _), square=0,
                 symbol=X) == (X, _, _, _, _, _, _, _, _)
assert get_board(board=(_, _, _, _, _, _, _, _, _), square=8,
                 symbol=O) == (_, _, _, _, _, _, _, _, O)

assert get_columns((0, 1, 2, 3, 4, 5, 6, 7, 8)) == [
    (0, 3, 6), (1, 4, 7), (2, 5, 8)]

assert get_diagonals((0, 1, 2, 3, 4, 5, 6, 7, 8)) == [(0, 4, 8), (2, 4, 6)]

assert get_flipped_board((0, 1, 2, 3, 4, 5, 6, 7, 8)
                         ) == (2, 1, 0, 5, 4, 3, 8, 7, 6)

assert not get_is_full((_, _, _, _, _, _, _, _, _))
assert not get_is_full((X, O, X, O, X, O, X, O, _))
assert not get_is_full((_, X, O, X, O, X, O, X, O))
assert get_is_full((X, O, X, O, X, O, X, O, X))

assert get_rotated_board((0, 1, 2, 3, 4, 5, 6, 7, 8)
                         ) == (6, 3, 0, 7, 4, 1, 8, 5, 2)

assert get_rows((0, 1, 2, 3, 4, 5, 6, 7, 8)) == [
    (0, 1, 2), (3, 4, 5), (6, 7, 8)]

assert get_squares(board=(X, O, _, X, O, _, X, O, _), symbol=X) == [0, 3, 6]
assert get_squares(board=(X, O, _, X, O, _, X, O, _), symbol=O) == [1, 4, 7]
assert get_squares(board=(_, _, _, _, _, _, _, _, _), symbol=X) == []
assert get_squares(board=(X, X, X, X, X, X, X, X, X), symbol=X) == [
    0, 1, 2, 3, 4, 5, 6, 7, 8]
