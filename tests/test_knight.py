import pytest
from unittest.mock import MagicMock
from Piece import Knight


@pytest.fixture()
def empty_game_state():
    # create an empty game state
    game_state = MagicMock()
    game_state.get_piece.return_value = None
    game_state.is_valid_piece.return_value = False
    return game_state


def test_get_valid_peaceful_moves_with_pawn_in_center(empty_game_state):
    # create a game state with a pawn in the center
    empty_game_state.get_piece.side_effect = lambda row, col: 'P' if row == 3 and col == 3 else None
    knight = Knight("", 3, 4, 'W')

    # call the get_valid_peaceful_moves method and check the result
    assert knight.get_valid_peaceful_moves(empty_game_state) == [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2),
                                                                 (5, 4)]


def test_get_valid_peaceful_moves_with_no_moves(empty_game_state):
    # create a game state with the knight in the corner
    empty_game_state.get_piece.side_effect = lambda row, col: None
    knight = Knight("", 0, 0, 'W')

    # call the get_valid_peaceful_moves method and check the result
    assert knight.get_valid_peaceful_moves(empty_game_state) == []


def test_get_valid_peaceful_moves_with_all_moves(empty_game_state):
    # create a game state with the knight in the center
    empty_game_state.get_piece.side_effect = lambda row, col: None
    knight = Knight("", 3, 3, 'W')

    # call the get_valid_peaceful_moves method and check the result
    assert knight.get_valid_peaceful_moves(empty_game_state) == [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2),
                                                                 (5, 4)]


def test_get_valid_piece_takes_with_no_takes(empty_game_state):
    # create a game state with no valid takes for the knight
    empty_game_state.is_valid_piece.side_effect = lambda row, col: False
    knight = Knight("", 3, 3, 'W')

    # call the get_valid_piece_takes method and check the result
    assert knight.get_valid_piece_takes(empty_game_state) == []


def test_get_valid_piece_takes_with_one_take(empty_game_state):
    # create a game state with one valid take for the knight
    empty_game_state.is_valid_piece.side_effect = lambda row, col: row == 2 and col == 1
    empty_game_state.get_piece.side_effect = lambda row, col: 'P' if row == 2 and col == 1 else None
    knight = Knight("", 3, 3, 'W')

    # call the get_valid_piece_takes method and check the result
    assert knight.get_valid_piece_takes(empty_game_state) == [(2, 1)]


def test_get_valid_piece_takes_with_multiple_takes(empty_game_state):
    # create a game state with multiple valid takes for the knight
    empty_game_state.is_valid_piece.side_effect = lambda row, col: row in [2, 4] and col in [1, 5]
    empty_game_state.get_piece.side_effect = lambda row, col: 'P' if row in [2, 4] and col in [1, 5] else None
    knight = Knight("", 3, 3, 'W')

    assert knight.get_valid_piece_takes(empty_game_state) == [(2, 1), (2, 5), (4, 1), (4, 5)]
