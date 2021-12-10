from typing import List, Tuple


def get_input() -> List[Tuple[List[str], List[str]]]:
    with open("./input/day-8.txt", 'r') as f:
        contents = [x.replace("\n", "").split("|") for x in f.readlines()]
    return [(x[0].strip(), x[1].strip()) for x in contents]

def part_one(input: List[Tuple[List[str], List[str]]]) -> int:
    total = 0
    for _, output_value in input:
        # Count 1's
        parts = output_value.split(" ")
        total += sum(1 for x in parts if len(x) == 2)
        # Count 4's
        total += sum(1 for x in parts if len(x) == 4)
        # Count 7's
        total += sum(1 for x in parts if len(x) == 3)
        # Count 8's
        total += sum(1 for x in parts if len(x) == 7)
    return total

def part_two(input: List[Tuple[List[str], List[str]]]):
    pass

if __name__ == "__main__":
    input = get_input()
    print(part_one(input))
