from pathlib import Path


def parse_input() -> list[list[int]]:
    inputs = []
    with open(Path(__file__).parent / "input.txt") as file:
        for line in file:
            input_elements = line.rstrip()
            temp = []
            for val in input_elements:
                temp.append(int(val))
            inputs.append(temp)

    return inputs


def solution_part_1(inputs: list[list[int]]) -> int:
    total = 0
    for row in inputs:
        max = 0
        second_max = 0
        row_size = len(row)
        for idx, col in enumerate(row):
            if col > max and idx <= row_size - 2:
                max = col
                second_max = 0
            else:
                if col > second_max:
                    second_max = col
        total += int(f"{str(max)}{str(second_max)}")
    return total


def solution_part_2(inputs: list[list[int]]) -> int:
    total = 0
    for row in inputs:
        accumulated_num_str = ""
        row_size = len(row)
        col_idx = 0
        nums_left = 11
        while len(accumulated_num_str) < 12:
            max_num = max(row[col_idx : row_size - nums_left])
            accumulated_num_str += str(max_num)
            col_idx += row[col_idx : row_size - nums_left].index(max_num) + 1
            nums_left -= 1
        total += int(accumulated_num_str)
    return total


if __name__ == "__main__":
    inputs = parse_input()
    print(f"Solution part 1: {solution_part_1(inputs)}")
    print(f"Solution part 2: {solution_part_2(inputs)}")
