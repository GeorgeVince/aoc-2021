from typing import List


def get_input() -> List[int]:
    with open("input/day-1.txt") as f:
        contents = f.readlines()
    return [int(x) for x in contents]


def part_1(input: List[int]) -> int:
    count = 0
    cur = input[0]
    for next in input[1:]:
        if next > cur:
            count += 1
        cur = next
    return count


def part_2(input: List[int]) -> int:
    count = 0
    cur_window = sum(input[0:3])
    for indx in range(1, len(input) - 1):
        next_window = sum(input[indx : indx + 3])
        if next_window > cur_window:
            count += 1
        cur_window = next_window
    return count


if __name__ == "__main__":
    input = get_input()
    print(part_1(input))
    print(part_2(input))

