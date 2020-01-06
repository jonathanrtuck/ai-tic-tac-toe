from board import Symbol
from game import get_is_draw, get_result, get_winner, Result

_ = Symbol.Empty
X = Symbol.X
O = Symbol.O


assert not get_is_draw((X, X, X, X, X, X, X, X, X))
assert not get_is_draw((O, O, O, _, _, _, _, _, _))
assert not get_is_draw((O, X, _, _, _, _, _, X, O))
assert get_is_draw((X, O, O, O, X, X, X, O, O))

assert get_result(player=X, winner=X) == Result.Win
assert get_result(player=X, winner=O) == Result.Loss
assert get_result(player=X, winner=None) == Result.Draw
assert get_result(player=O, winner=O) == Result.Win
assert get_result(player=O, winner=X) == Result.Loss
assert get_result(player=O, winner=None) == Result.Draw

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
