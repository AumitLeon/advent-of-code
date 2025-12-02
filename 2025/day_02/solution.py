from collections import Counter
from pathlib import Path


def parse_input() -> list[tuple[int, int]]:
    inputs = []
    with open(Path(__file__).parent / "input.txt") as file:
        for line in file:
            input_elements = line.rstrip().split(",")

            for vals in input_elements:
                split_vals = vals.split("-")
                inputs.append((int(split_vals[0]), int(split_vals[1])))
    return inputs


def is_invalid_id(id: str) -> bool:
    middle_index = round(len(id) / 2)
    return id[:middle_index] == id[middle_index:]


def solution_part_1(inputs):
    invalid_ids = []
    for val in inputs:
        for i in range(val[0], val[1] + 1):
            if len(str(i)) % 2 != 0:
                continue
            else:
                if is_invalid_id(str(i)):
                    invalid_ids.append(i)
    return sum(invalid_ids)


def test_validity(id: str) -> bool:
    middle_index = round(len(id) / 2)
    for i in range(2, middle_index + 1):
        if i == 1:
            break
        if (int(id) % int(id[:i]) == 0) and str(round((int(id) / int(id[:i]))))[-1] == "1":
            id_split = id.split(id[:i])
            # When splitting by the repeated number, there shouldn't be anything other than empty strings in the split.
            # Also, the split will produce 1 more than the number of times the number is repeated because of the last split.
            if len(id_split) - 1 == round(len(id) / len(id[:i])) and all(
                val == "" for val in id_split
            ):
                return True
    return False


def is_invalid_id_part_2(id: str) -> bool:
    # If the number is a full repeat, auto invalid.
    counter = Counter(id)
    if len(counter) == 1 and len(id) > 1:
        return True
    elif len(counter) > 1 and len(id) % 2 != 0 and len(id) < 9:
        return False
    else:
        return test_validity(id)


def solution_part_2(inputs: list[tuple[int, int]]):
    invalid_ids = []
    for val in inputs:
        curr_invalids = []
        for i in range(val[0], val[1] + 1):
            if is_invalid_id_part_2(str(i)):
                invalid_ids.append(i)
                curr_invalids.append(i)

    return sum(set(invalid_ids))


if __name__ == "__main__":
    inputs = parse_input()
    print(f"Solution part 1: {solution_part_1(inputs)}")
    print(f"Solution part 2: {solution_part_2(inputs)}")
