from dataclasses import dataclass
from typing import List


@dataclass
class TargetArea:
    x1: int
    x2: int
    y1: int
    y2: int


@dataclass
class Coordinate:
    x: int
    y: int


def path(start_coordinate, max_y) -> List[Coordinate]:
    coords = [Coordinate(0, 0)]
    x, y = start_coordinate.x, start_coordinate.y
    rel_x, rel_y = x, y

    while rel_y >= max_y:
        if x > 0:
            x -= 1
        y -= 1

        coords.append(Coordinate(rel_x, rel_y))
        rel_x = rel_x + x
        rel_y = rel_y + y
    return coords


def valid_path(coords, target) -> bool:
    return any(in_target(coord, target) for coord in coords[::-1])


def in_target(coord: Coordinate, target: TargetArea) -> bool:   
    return (coord.x >= target.x1
            and coord.x <= target.x2
            and coord.y >= target.y1
            and coord.y <= target.y2)


def all_valid_paths(target) -> List[List[Coordinate]]:
    valid = []
    for x in range(0, target.x2 + 1):
        for y in range(target.y1, abs(target.y1)):
            _path = path(Coordinate(x, y), target.y1)
            if valid_path(_path, target):
                valid.append(_path)
    return valid


def part_one(input) -> int:
    target = parse_target(input)
    valid_paths = all_valid_paths(target)
    max_y = max(max(coord.y for coord in path)for path in valid_paths)
    return max_y

def part_two(input) -> int:
    # Can just brute force this too
    target = parse_target(input)
    valid_paths = all_valid_paths(target)
    return len(valid_paths)


def parse_target(input) -> TargetArea:
    x, y = input.split(",")
    x1 = x.split("..")[0].split("=")[1]
    x2 = x.split("..")[1]
    y1 = y.split("..")[0].split("=")[1]
    y2 = y.split("..")[1]

    return TargetArea(int(x1), int(x2), int(y1), int(y2))


def get_input():
    with open('input/day-17.txt', 'r') as f:
        contents = f.read().strip()
    return contents


if __name__ == "__main__":
    input = get_input()
    # Can brute force both
    print(part_one(input))
    print(part_two(input))
