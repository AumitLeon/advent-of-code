from pathlib import Path


def parse_input() -> tuple[list[list[str]], list[tuple[int, int]]]:
    matrix = []  # (row, col)
    roll_coords = []
    with open(Path(__file__).parent / "input.txt") as file:
        row_cnt = 0
        for line in file:
            input_elements = line.rstrip()
            temp = []
            for idx, char in enumerate(input_elements):
                if char == "@":
                    roll_coords.append((row_cnt, idx))
                temp.append(char)
            row_cnt += 1

            matrix.append(temp)

    return matrix, roll_coords


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


def get_accessible_rolls(
    matrix: list[list[str]], roll_coords: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    count = 0
    accessible_roll_coords = []
    set_roll_coords = set(roll_coords)
    for row, col in roll_coords:
        adjacent_rolls = 0
        for adjacent_row, adjacent_col in get_adjacent_positions(row, col):
            if is_valid_position(adjacent_row, adjacent_col, matrix):
                if (adjacent_row, adjacent_col) in set_roll_coords:
                    adjacent_rolls += 1
        if adjacent_rolls < 4:
            accessible_roll_coords.append((row, col))
            count += 1
    return accessible_roll_coords


def get_total_possible_accessible_rolls_removed(
    matrix: list[list[str]], roll_coords: list[tuple[int, int]]
) -> int:
    rolls_removed = 0
    accessible_roll_coords = get_accessible_rolls(matrix, roll_coords)
    while len(accessible_roll_coords) > 0:
        # mark the currently accessible rolls as x's.
        for row, col in accessible_roll_coords:
            matrix[row][col] = "."
            roll_coords.remove((row, col))
            rolls_removed += 1
        accessible_roll_coords = get_accessible_rolls(matrix, roll_coords)

    return rolls_removed


if __name__ == "__main__":
    matrix, roll_coords = parse_input()
    print(f"Solution part 1: {len(get_accessible_rolls(matrix, roll_coords))}")
    print(f"Solution part 2: {get_total_possible_accessible_rolls_removed(matrix, roll_coords)}")
