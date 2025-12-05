from .solution import (
    get_accessible_rolls,
    get_total_possible_accessible_rolls_removed,
    parse_input,
)


def test_parse_input():
    matrix, roll_coords = parse_input()
    assert len(matrix[0]) == 139
    assert len(matrix) == 139
    assert len(roll_coords) == 12709


def test_solution_part_1():
    matrix, roll_coords = parse_input()
    assert len(get_accessible_rolls(matrix, roll_coords)) == 1346


def test_solution_part_2():
    matrix, roll_coords = parse_input()
    assert get_total_possible_accessible_rolls_removed(matrix, roll_coords) == 8493
