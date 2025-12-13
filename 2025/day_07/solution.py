from pathlib import Path


def parse_input() -> tuple[list[list[str]], set[tuple[int, int]], tuple[int, int]]:
    matrix = []  # (row, col)
    start_position = None
    splitter_positions = []
    with open(Path(__file__).parent / "input.txt") as file:
        row_cnt = 0
        for line in file:
            input_elements = line.rstrip()
            temp = []
            for idx, char in enumerate(input_elements):
                if char == "S":
                    start_position = (row_cnt, idx)
                elif char == "^":
                    splitter_positions.append((row_cnt, idx))

                temp.append(char)
            row_cnt += 1

            matrix.append(temp)

    return matrix, set(splitter_positions), start_position


def get_adjacent_positions(row_idx: int, column_idx: int) -> list[tuple[int, int]]:
    return [
        (row_idx + 1, column_idx),  # Below
        (row_idx - 1, column_idx),  # Above
        (row_idx, column_idx + 1),  # Right
        (row_idx, column_idx - 1),  # Left
        (row_idx - 1, column_idx - 1),  # Top left
        (row_idx - 1, column_idx + 1),  # Top right
        (row_idx + 1, column_idx + 1),  # Bottom right
        (row_idx + 1, column_idx - 1),  # Bottom left
    ]


def is_valid_position(row: int, col: int, matrix: list[list[str]]) -> bool:
    matrix_row_dimension = len(matrix)
    matrix_col_dimension = len(matrix[0])
    if 0 > col or col > matrix_col_dimension - 1 or 0 > row or row > matrix_row_dimension - 1:
        return False
    else:
        return True


def is_valid_beam_position(row: int, col: int, matrix: list[list[str]]) -> bool:
    matrix_row_dimension = len(matrix)
    matrix_col_dimension = len(matrix[0])
    if 0 > col or col > matrix_col_dimension - 1 or 0 > row or row > matrix_row_dimension - 1:
        return False
    else:
        return True


def get_split_positions(splitter_row: int, splitter_col: int, matrix: list[list[str]]):
    split_positions = []
    if is_valid_beam_position(splitter_row, splitter_col - 1, matrix):
        split_positions.append((splitter_row, splitter_col - 1))
    if is_valid_beam_position(splitter_row, splitter_col + 1, matrix):
        split_positions.append((splitter_row, splitter_col + 1))
    return split_positions


def solution(
    matrix: list[list[str]],
    splitter_positions: set[tuple[int, int]],
    start_position: tuple[int, int],
):
    split_counter = 0
    beam_cntr = 0
    beam_positions = [(start_position[0], start_position[1])]
    timelines = [[0 for _ in row] for row in matrix]

    timelines[start_position[0]][start_position[1]] = 1
    for idx, _ in enumerate(matrix):
        temp_positions = []
        for beam_row, beam_col in beam_positions:
            next_row = beam_row + 1  # below
            next_col = beam_col
            next_pos = (next_row, next_col)

            if is_valid_position(next_row, next_col, matrix):
                if matrix[next_row][next_col] == ".":
                    matrix[next_row][next_col] = "|"
                    temp_positions.append(next_pos)
                    beam_cntr += 1
                    timelines[next_row][next_col] += timelines[beam_row][beam_col]
                elif matrix[next_row][next_col] == "|":
                    timelines[next_row][next_col] += timelines[beam_row][beam_col]
                    temp_positions.append(next_pos)
                elif matrix[next_row][next_col] == "^":
                    split_counter += 1
                    splitter_positions = get_split_positions(next_row, next_col, matrix)

                    for split_row, split_col in splitter_positions:
                        matrix[split_row][split_col] = "|"
                        beam_cntr += 1
                        temp_positions.append((split_row, split_col))

                        timelines[split_row][split_col] += timelines[beam_row][beam_col]

        beam_positions = set(temp_positions)

    return split_counter, sum(timelines[-1])


if __name__ == "__main__":
    matrix, splitter_positions, start_position = parse_input()
    part_1, part_2 = solution(matrix, splitter_positions, start_position)
    print(f"Solution part 1: {part_1}")
    print(f"Solution part 2: {part_2}")
