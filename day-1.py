from typing import List

def get_input() -> List[int]:
    with open('input/day-1.txt') as f:
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


if __name__ == "__main__":
    input = get_input()
    print(part_1(input))
    