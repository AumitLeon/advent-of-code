from math import floor
from pathlib import Path
from typing import List, Tuple


def parse_input() -> List[Tuple[str, int]]:
    inputs = []
    with open(Path(__file__).parent / "input.txt") as file:
        for line in file:
            input_elements = line.rstrip().split("  ")
            direction = input_elements[0][0]
            distance = int(input_elements[0][1:])
            inputs.append((direction, distance))
    return inputs


def compute_new_position_part_2(
    curr_position: int, direction: str, distance: int
) -> Tuple[int, int]:
    num_zeroes = 0
    if direction == "R":
        adjusted_distance = distance % 100
        num_rotations = floor(distance / 100)
        num_zeroes += num_rotations
        if curr_position + adjusted_distance > 99:
            temp = curr_position + adjusted_distance
            new_position = temp - 100
            if new_position != 0:
                num_zeroes += 1

            curr_position = temp - 100
        else:
            new_position = curr_position + adjusted_distance

            curr_position += adjusted_distance
    elif direction == "L":
        adjusted_distance = distance % 100
        num_rotations = floor(distance / 100)
        num_zeroes += num_rotations
        if curr_position - adjusted_distance < 0:
            temp = abs(curr_position - adjusted_distance)
            if curr_position != 0:
                num_zeroes += 1
            new_position = 100 - temp
            curr_position = 100 - temp
        else:
            new_position = curr_position - adjusted_distance
            curr_position -= adjusted_distance
    return curr_position, num_zeroes


def compute_new_position_part_1(curr_position: int, direction: str, distance: int) -> int:
    if direction == "R":
        adjusted_distance = distance % 100
        if curr_position + adjusted_distance > 99:
            temp = curr_position + adjusted_distance
            curr_position = temp - 100
        else:
            curr_position += adjusted_distance
    elif direction == "L":
        adjusted_distance = distance % 100
        if curr_position - adjusted_distance < 0:
            temp = abs(curr_position - adjusted_distance)
            curr_position = 100 - temp
        else:
            curr_position -= adjusted_distance
    return curr_position


def solution_part_2(inputs: List[Tuple[str, int]]) -> int:
    curr_position = 50
    counter = 0
    for direction, distance in inputs:
        curr_position, num_zeroes = compute_new_position_part_2(curr_position, direction, distance)
        counter += num_zeroes
        if curr_position == 0:
            counter += 1
    return counter


def solution_part_1(inputs: List[Tuple[str, int]]) -> int:
    curr_position = 50
    counter = 0
    for direction, distance in inputs:
        curr_position = compute_new_position_part_1(curr_position, direction, distance)
        if curr_position == 0:
            counter += 1
    return counter


if __name__ == "__main__":
    inputs = parse_input()
    print(f"Solution part 1: {solution_part_1(inputs)}")
    print(f"Solution part 2: {solution_part_2(inputs)}")
