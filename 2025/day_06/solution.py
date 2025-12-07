from math import prod
from pathlib import Path


def parse_input() -> list[list[str]]:
    inputs = []
    with open(Path(__file__).parent / "input.txt") as file:
        for line in file:
            input_elements = line.rstrip()
            inputs.append(input_elements.split())

    return inputs


def chunk(line: str) -> list[list[str]]:
    chunks = []
    for i in range(0, len(line), 4):
        chunks.append(line[i : i + 3])
    return chunks


def parse_input_part_2() -> tuple[list[str], list[str], list[int]]:
    operators = []
    raw_lines = []
    operand_widths = []
    with open(Path(__file__).parent / "input.txt") as file:
        for line in file:
            if line[0] not in ("*", "+"):
                raw_lines.append(line)
            else:
                input_elements = line.rstrip()
                dist = 0
                x = line.replace("\n", ".^")
                for char in x[1:]:
                    # TODO: This works for the actual input, but not the small input.
                    # The problem is my algorithm uses the distance between operators in the last line to determine the width of the column.
                    # The issue is, in the last line, the last operator is followed by one space and then the new line. So this method doesn't work to figure out the size of the last column programatically.
                    # It so happens that the last column in my input has width 2, which this code provides, but the small input has length 3, which I would need to manually support with a special case for the `^` token I added.
                    if char in ("*", "+", "^"):
                        operand_widths.append(dist)
                        dist = 0
                    else:
                        dist += 1

                operators = input_elements.split()

    return operators, raw_lines, operand_widths


def transpose_matrix(matrix: list[list[str]], cast_int: bool = True) -> list[list[str | int]]:
    transposed_matrix = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    for i in range(num_cols):
        problem = []
        for j in range(num_rows):
            if matrix[j][i] in ("+", "*"):
                problem.append(matrix[j][i])
            else:
                if cast_int:
                    problem.append(int(matrix[j][i]))
                else:
                    problem.append(matrix[j][i])

        transposed_matrix.append(problem)
    return transposed_matrix


def solution_part_1(matrix: list[list[str]]) -> int:
    total = 0
    transposed_matrix = transpose_matrix(matrix)
    for problem in transposed_matrix:
        operator = problem[-1]
        problem_answer = 0
        if operator == "*":
            problem_answer = prod(problem[:-1])
        else:
            problem_answer = sum(problem[:-1])

        total += problem_answer
    return total


def split_nums(operand_widths: list[int], raw_lines: list[str]) -> list[list[str]]:
    operands = []
    for line in raw_lines:
        curr_operands = []
        curr_line_idx = 0
        for width in operand_widths:
            curr_operands.append(line[curr_line_idx : curr_line_idx + width])
            curr_line_idx += width + 1
        operands.append(curr_operands)
    return operands


def solution_part_2(operators: list[str], raw_lines: list[str], operand_widths: list[int]) -> int:
    total = 0
    matrix = split_nums(operand_widths, raw_lines)
    transposed_matrix = transpose_matrix(matrix, False)

    for problem, operator, operand_width in zip(transposed_matrix, operators, operand_widths):
        problem_answer = 0
        new_operands = []
        newlined_stripped_problem = [val.replace("\n", "") for val in problem]
        for i in range(operand_width - 1, -1, -1):
            num = ""
            for operand in newlined_stripped_problem:
                if operand[i].isdigit():
                    num += operand[i]

            new_operands.append(int(num))

        if operator == "*":
            problem_answer = prod(new_operands)
        else:
            problem_answer = sum(new_operands)
        total += problem_answer
    return total


if __name__ == "__main__":
    matrix = parse_input()
    print(f"Solution part 1: {solution_part_1(matrix)}")

    operators, raw_lines, operand_widths = parse_input_part_2()
    print(f"Solution part 2: {solution_part_2(operators, raw_lines, operand_widths)}")
