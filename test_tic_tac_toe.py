from tic_tac_toe import *

assert get_column((0, 1, 2, 3, 4, 5, 6, 7, 8), 0) == (0, 3, 6)
assert get_column((0, 1, 2, 3, 4, 5, 6, 7, 8), 1) == (1, 4, 7)
assert get_column((0, 1, 2, 3, 4, 5, 6, 7, 8), 2) == (2, 5, 8)

assert get_flipped_square(0) == 2
assert get_flipped_square(1) == 1
assert get_flipped_square(2) == 0
assert get_flipped_square(3) == 5
assert get_flipped_square(4) == 4
assert get_flipped_square(5) == 3
assert get_flipped_square(6) == 8
assert get_flipped_square(7) == 7
assert get_flipped_square(8) == 6

assert get_flipped_squares((0, 1, 2, 3, 4, 5, 6, 7, 8)) == (
    2, 1, 0, 5, 4, 3, 8, 7, 6)

assert not get_is_draw(('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'))
assert get_is_draw(('x', 'o', 'o', 'o', 'x', 'x', 'x', 'o', 'o'))

assert not get_is_full((' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '))
assert not get_is_full(('x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', ' '))
assert get_is_full(('x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x'))

assert get_is_over(('x', 'o', 'o', 'o', 'x', 'x', 'x', 'o', 'o'))
assert get_is_over(('x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x'))
assert get_is_over(('x', 'x', 'x', 'o', 'o', ' ', ' ', ' ', ' '))
assert not get_is_over(('x', 'x', 'o', 'o', 'o', ' ', ' ', ' ', ' '))

assert get_normalized_square('x', 'x') == 'm'
assert get_normalized_square('x', 'o') == 'y'
assert get_normalized_square('o', 'o') == 'm'
assert get_normalized_square('o', 'x') == 'y'
assert get_normalized_square(' ', 'x') == ' '
assert get_normalized_square(' ', 'o') == ' '

assert get_normalized_squares(('x', 'x', 'x', 'o', 'o', 'o', ' ', ' ', ' '), 'x') == (
    'm', 'm', 'm', 'y', 'y', 'y', ' ', ' ', ' ')

assert get_other_char('x') == 'o'
assert get_other_char('o') == 'x'
assert get_other_char(' ') == None

assert get_rotate_square(0) == 2
assert get_rotate_square(1) == 5
assert get_rotate_square(2) == 8
assert get_rotate_square(3) == 1
assert get_rotate_square(4) == 4
assert get_rotate_square(5) == 7
assert get_rotate_square(6) == 0
assert get_rotate_square(7) == 3
assert get_rotate_square(8) == 6

assert get_rotate_squares((0, 1, 2, 3, 4, 5, 6, 7, 8)
                          ) == (6, 3, 0, 7, 4, 1, 8, 5, 2)

assert get_row((0, 1, 2, 3, 4, 5, 6, 7, 8), 0) == (0, 1, 2)
assert get_row((0, 1, 2, 3, 4, 5, 6, 7, 8), 1) == (3, 4, 5)
assert get_row((0, 1, 2, 3, 4, 5, 6, 7, 8), 2) == (6, 7, 8)

assert get_squares(('x', 'o', ' ', 'x', 'o', ' ',
                    'x', 'o', ' '), 'x') == [0, 3, 6]
assert get_squares(('x', 'o', ' ', 'x', 'o', ' ',
                    'x', 'o', ' '), 'o') == [1, 4, 7]
assert get_squares((' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '), 'x') == []
assert get_squares(('x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'), 'x') == [
    0, 1, 2, 3, 4, 5, 6, 7, 8]

assert get_weight_key((' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '),
                      0) == "(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')0"
assert get_weight_key(('x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', ' '),
                      8) == "('x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', ' ')8"

assert get_winner((' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')) == None
assert get_winner((' ', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ')) == None
assert get_winner((' ', ' ', ' ', ' ', 'o', 'o', 'o', ' ', ' ')) == None
assert get_winner(('x', 'o', 'o', 'o', 'x', 'x', 'x', 'o', 'o')) == None
assert get_winner(('x', ' ', ' ', 'x', ' ', ' ', 'x', ' ', ' ')) == 'x'
assert get_winner((' ', 'o', ' ', ' ', 'o', ' ', ' ', 'o', ' ')) == 'o'
assert get_winner(('x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ')) == 'x'
assert get_winner((' ', ' ', ' ', 'o', 'o', 'o', ' ', ' ', ' ')) == 'o'
assert get_winner(('x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x')) == 'x'
assert get_winner((' ', ' ', 'o', ' ', 'o', ' ', 'o', ' ', ' ')) == 'o'
