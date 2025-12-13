from .solution import (
    parse_input,
    solution,
)


def test_parse_input():
    matrix, splitter_positions, start_position = parse_input()
    assert len(matrix[0]) == 141
    assert len(matrix) == 142
    assert len(splitter_positions) == 1689
    assert start_position == (0, 70)


def test_solution():
    matrix, splitter_positions, start_position = parse_input()
    part_1, part_2 = solution(matrix, splitter_positions, start_position)
    assert part_1 == 1581
    assert part_2 == 73007003089792
