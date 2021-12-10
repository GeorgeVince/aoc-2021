from typing import List


def get_input() -> int:
    with open("./input/day-7.txt", 'r') as f:
        contents = f.read()
    return [int(x) for x in contents.split(",")]


def find_distance(num: int, input: List[int]):
    difference = 0
    for x in input:
        difference += abs(x-num)
    return difference


def find_distance_part_two(num: int, input: List[int]):
    difference = 0
    for x in input:
        difference += (0.5 * abs(x-num)) * (abs(x-num) + 1)
    return difference


def part_one(input: List[int]):
    distances = {}
    for x in range(min(input), max(input)):
        distances[x] = distances.get(x, find_distance(x, input))

    return distances[min(distances, key=distances.get)]

def part_two(input: List[int]):
    distances = {}
    for x in range(min(input), max(input)):
        distances[x] = distances.get(x, find_distance_part_two(x, input))

    return distances[min(distances, key=distances.get)]


if __name__ == "__main__":
    input = get_input()
    print(part_one(input))
    print(part_two(input))
