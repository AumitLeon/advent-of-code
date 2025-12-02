from .solution import (
    get_number_of_safe_reports_part_1,
    get_number_of_safe_reports_part_2,
    parse_input,
)


def test_parse_input():
    assert len(parse_input()) == 1000


def test_get_number_of_safe_report_v2():
    parsed_input = parse_input()
    assert get_number_of_safe_reports_part_1(parsed_input) == 486


def test_get_number_of_safe_reports_part_2():
    parsed_input = parse_input()
    assert get_number_of_safe_reports_part_2(parsed_input) == 540
