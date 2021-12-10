from dataclasses import dataclass
from typing import Counter, List


def get_input() -> int:
    with open("./input/day-6.txt", 'r') as f:
        contents = f.read()
    return [int(x) for x in contents.split(",")]


def simulate(initial_ages: List[int], num_days: int) -> int:
    age_occurances = {day_val: initial_ages.count(
        day_val) for day_val in range(-1, 9)}

    for _ in range(0, num_days):
        age_occurances = {k-1: v for k, v in age_occurances.items() if k >= 0}

        age_occurances[8] = age_occurances.get(-1, 0)
        age_occurances[6] += age_occurances.get(-1, 0)
        age_occurances[-1] = 0

    return sum(age_occurances.values())

def part_one(input: List[int], num_days: int) -> int:
    return simulate(input, 80)

def part_two(input: List[int], num_days: int) -> int:
    return simulate(input, 256)

if __name__ == "__main__":
    input = get_input()
    print(part_one(input, 80))
    print(part_two(input, 256))