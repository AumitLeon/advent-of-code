from pathlib import Path


def parse_input() -> tuple[list[tuple[int, int]], list[int]]:
    processing_available_ingredients = False
    ranges = []
    nums = []
    with open(Path(__file__).parent / "input.txt") as file:
        for line in file:
            input_elements = line.rstrip()
            if input_elements == "":
                processing_available_ingredients = True
                continue

            if not processing_available_ingredients:
                split_vals = input_elements.split("-")
                ranges.append((int(split_vals[0]), int(split_vals[1])))
            else:
                nums.append(int(input_elements))

    return ranges, nums


def solution_part_1(ranges: list[tuple[int, int]], nums: list[int]) -> int:
    count = 0
    set_of_ranges = set(ranges)
    for num in nums:
        for start, end in set_of_ranges:
            if start <= num <= end:
                count += 1
                break
    return count


def solution_part_2(ranges: list[tuple[int, int]]) -> int:
    num_fresh = 0
    deduped_ranges = list(set(ranges))

    consolidation_found = True
    comparison_merged = False
    merged_ranges = set(deduped_ranges).copy()
    while consolidation_found:
        for range in merged_ranges:
            temp = merged_ranges.copy()
            temp.remove(range)

            if not temp:
                consolidation_found = False
                break
            for sub_range in temp:
                if range[0] < sub_range[0] and sub_range[0] < range[0] < sub_range[1]:
                    comparison_merged = True
                    new_range = (range[0], sub_range[1])
                elif (
                    sub_range[1] > range[0] >= sub_range[0]
                    and sub_range[0] < range[1] >= sub_range[1]
                ):
                    comparison_merged = True
                    new_range = (sub_range[0], range[1])
                elif (
                    sub_range[0] <= range[0] < sub_range[1]
                    and sub_range[0] < range[1] < sub_range[1]
                ):
                    new_range = sub_range
                    comparison_merged = True
                elif (
                    sub_range[0] >= range[0] < sub_range[1]
                    and sub_range[0] < range[1] > sub_range[1]
                ):
                    new_range = range
                    comparison_merged = True
                elif range[0] == sub_range[1]:
                    new_range = (sub_range[0], range[1])
                    comparison_merged = True
                elif range[1] == sub_range[0]:
                    new_range = (range[0], sub_range[1])
                    comparison_merged = True

                if comparison_merged:
                    temp.remove(sub_range)
                    temp.add(new_range)
                    merged_ranges = temp
                    break
                else:
                    consolidation_found = False
            if comparison_merged:
                consolidation_found = True
                comparison_merged = False
                break

    for start, end in set(merged_ranges):
        num_fresh += end - start + 1

    return num_fresh


if __name__ == "__main__":
    ranges, nums = parse_input()

    print(f"Solution part 1: {solution_part_1(ranges, nums)}")
    print(f"Solution part 2: {solution_part_2(ranges)}")
