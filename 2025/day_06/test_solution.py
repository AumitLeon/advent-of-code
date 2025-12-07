from .solution import parse_input, parse_input_part_2, solution_part_1, solution_part_2


def test_parse_input():
    matrix = parse_input()
    assert len(matrix) == 5
    assert len(matrix[0]) == 1000


def test_parse_input_part_2():
    operators, raw_lines, operand_widths = parse_input_part_2()
    assert len(operators) == 1000
    assert len(raw_lines) == 4
    assert len(operand_widths) == 1000


def test_solution_part_1():
    matrix = parse_input()
    assert solution_part_1(matrix) == 5782351442566


def test_solution_part_2():
    operators, raw_lines, operand_widths = parse_input_part_2()
    assert solution_part_2(operators, raw_lines, operand_widths) == 10194584711842
