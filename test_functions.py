from enums import Result, Symbol
from functions import (get_board, get_columns, get_diagonals, get_flipped_board, get_is_draw, get_is_full,
                       get_normalized_board, get_other_player, get_position, get_result, get_rotated_board, get_rows, get_squares, get_winner)

_ = Symbol.Empty
X = Symbol.X
O = Symbol.O
M = Symbol.Me
Y = Symbol.Opponent
C = Symbol.Considering

assert get_columns((0, 1, 2, 3, 4, 5, 6, 7, 8)) == [
    (0, 3, 6), (1, 4, 7), (2, 5, 8)]

assert get_diagonals((0, 1, 2, 3, 4, 5, 6, 7, 8)) == [(0, 4, 8), (2, 4, 6)]

assert get_flipped_board((0, 1, 2, 3, 4, 5, 6, 7, 8)
                         ) == (2, 1, 0, 5, 4, 3, 8, 7, 6)

assert not get_is_draw((X, X, X, X, X, X, X, X, X))
assert not get_is_draw((O, O, O, _, _, _, _, _, _))
assert not get_is_draw((O, X, _, _, _, _, _, X, O))
assert get_is_draw((X, O, O, O, X, X, X, O, O))

assert not get_is_full((_, _, _, _, _, _, _, _, _))
assert not get_is_full((X, O, X, O, X, O, X, O, _))
assert not get_is_full((_, X, O, X, O, X, O, X, O))
assert get_is_full((X, O, X, O, X, O, X, O, X))

assert get_normalized_board(board=(X, X, X, O, O, O, _, _, _), player=X) == (
    M, M, M, Y, Y, Y, _, _, _)

assert get_other_player(X) == O
assert get_other_player(O) == X
assert get_other_player(_) == None

assert get_position(board=(_, _, _, _, _, _, _, _, _),
                    square=0, player=X) == (_, _, _, _, _, _, _, _, C)
assert get_position(board=(X, _, O, _, X, X, _, O, _),
                    square=6, player=O) == (_, M, C, Y, Y, _, M, _, Y)

assert get_result(player=X, winner=X) == Result.Win
assert get_result(player=X, winner=O) == Result.Loss
assert get_result(player=X, winner=None) == Result.Draw
assert get_result(player=O, winner=O) == Result.Win
assert get_result(player=O, winner=X) == Result.Loss
assert get_result(player=O, winner=None) == Result.Draw

assert get_rotated_board((0, 1, 2, 3, 4, 5, 6, 7, 8)
                         ) == (6, 3, 0, 7, 4, 1, 8, 5, 2)

assert get_rows((0, 1, 2, 3, 4, 5, 6, 7, 8)) == [
    (0, 1, 2), (3, 4, 5), (6, 7, 8)]

assert get_squares(board=(X, O, _, X, O, _, X, O, _), symbol=X) == [0, 3, 6]
assert get_squares(board=(X, O, _, X, O, _, X, O, _), symbol=O) == [1, 4, 7]
assert get_squares(board=(_, _, _, _, _, _, _, _, _), symbol=X) == []
assert get_squares(board=(X, X, X, X, X, X, X, X, X), symbol=X) == [
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

assert get_board(board=(_, _, _, _, _, _, _, _, _), square=0,
                 symbol=X) == (X, _, _, _, _, _, _, _, _)
assert get_board(board=(_, _, _, _, _, _, _, _, _), square=8,
                 symbol=O) == (_, _, _, _, _, _, _, _, O)
