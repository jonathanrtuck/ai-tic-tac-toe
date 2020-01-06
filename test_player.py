from board import Symbol
from player import get_normalized_board, get_other_player, get_position, Square

_ = Symbol.Empty
X = Symbol.X
O = Symbol.O

E = Square.Empty
M = Square.Mine
Y = Square.Yours
C = Square.Considering


assert get_normalized_board(board=(X, X, X, O, O, O, _, _, _), player=X) == (
    M, M, M, Y, Y, Y, _, _, _)

assert get_other_player(X) == O
assert get_other_player(O) == X
assert get_other_player(_) == None

assert get_position(board=(_, _, _, _, _, _, _, _, _),
                    square=0, player=X) == (E, E, E, E, E, E, E, E, C)
assert get_position(board=(X, _, O, _, X, X, _, O, _),
                    square=6, player=O) == (E, M, C, Y, Y, E, M, E, Y)
