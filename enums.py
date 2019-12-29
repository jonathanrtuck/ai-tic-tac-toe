from enum import IntEnum


class Result(IntEnum):
    Win = 1
    Loss = -1
    Draw = 0


class Symbol(IntEnum):
    Empty = 0
    X = 1
    O = 2
    Me = 3
    Opponent = 4
    Considering = 5
