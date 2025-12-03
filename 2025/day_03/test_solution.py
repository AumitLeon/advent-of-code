from .solution import parse_input, solution_part_1, solution_part_2


def test_parse_input():
    inputs = parse_input()
    assert len(inputs) == 200


def test_solution_part_1():
    inputs = parse_input()
    assert solution_part_1(inputs) == 17034


def test_solution_part_2():
    inputs = parse_input()
    assert solution_part_2(inputs) == 168798209663590
