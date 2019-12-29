from enums import Result, Symbol
from functions import (get_board, get_columns, get_diagonals, get_is_draw, get_is_full, get_normalized_board,
                       get_other_player, get_position, get_result, get_rows, get_squares, get_winner)

_ = Symbol.Empty
X = Symbol.X
O = Symbol.O

assert get_columns((0, 1, 2, 3, 4, 5, 6, 7, 8)) == [
    (0, 3, 6), (1, 4, 7), (2, 5, 8)]

assert get_diagonals((0, 1, 2, 3, 4, 5, 6, 7, 8)) == [(0, 4, 8), (2, 4, 6)]

assert not get_is_draw((X, X, X, X, X, X, X, X, X))
assert not get_is_draw((O, O, O, _, _, _, _, _, _))
assert not get_is_draw((O, X, _, _, _, _, _, X, O))
assert get_is_draw((X, O, O, O, X, X, X, O, O))

assert not get_is_full((_, _, _, _, _, _, _, _, _))
assert not get_is_full((X, O, X, O, X, O, X, O, _))
assert not get_is_full((_, X, O, X, O, X, O, X, O))
assert get_is_full((X, O, X, O, X, O, X, O, X))

# TODO get_normalized_board

assert get_other_player(X) == O
assert get_other_player(O) == X
assert get_other_player(_) == None

# TODO get_position

assert get_result(X, X) == Result.Win
assert get_result(O, O) == Result.Win
assert get_result(X, O) == Result.Loss
assert get_result(O, X) == Result.Loss
assert get_result(X, None) == Result.Draw
assert get_result(O, None) == Result.Draw

assert get_rows((0, 1, 2, 3, 4, 5, 6, 7, 8)) == [
    (0, 1, 2), (3, 4, 5), (6, 7, 8)]

assert get_squares((X, O, _, X, O, _, X, O, _), X) == [0, 3, 6]
assert get_squares((X, O, _, X, O, _, X, O, _), O) == [1, 4, 7]
assert get_squares((_, _, _, _, _, _, _, _, _), X) == []
assert get_squares((X, X, X, X, X, X, X, X, X), X) == [
    0, 1, 2, 3, 4, 5, 6, 7, 8]

assert get_winner((_, _, _, _, _, _, _, _, _)) == None
assert get_winner((_, X, X, X, _, _, _, _, _)) == None
assert get_winner((_, _, _, _, O, O, O, _, _)) == None
assert get_winner((X, O, O, O, X, X, X, O, O)) == None
assert get_winner((X, _, _, X, _, _, X, _, _)) == X
assert get_winner((_, O, _, _, O, _, _, O, _)) == O
assert get_winner((X, X, X, _, _, _, _, _, _)) == X
assert get_winner((_, _, _, O, O, O, _, _, _)) == O
assert get_winner((X, _, _, _, X, _, _, _, X)) == X
assert get_winner((_, _, O, _, O, _, O, _, _)) == O

assert get_board((_, _, _, _, _, _, _, _, _), 0,
                 X) == (X, _, _, _, _, _, _, _, _)
assert get_board((_, _, _, _, _, _, _, _, _), 8,
                 O) == (_, _, _, _, _, _, _, _, O)
