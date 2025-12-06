from .solution import parse_input, solution_part_1, solution_part_2


def test_parse_input():
    ranges, nums = parse_input()
    assert len(ranges) == 195
    assert len(nums) == 1000


def test_solution_part_1():
    ranges, nums = parse_input()
    assert solution_part_1(ranges, nums) == 720


def test_solution_part_2():
    ranges, _ = parse_input()
    assert solution_part_2(ranges) == 357608232770687
