from dataclasses import dataclass, field
from typing import List
from collections import Counter


@dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

    @property
    def is_horizontal_or_vertical(self) -> bool:
        return (self.x1 == self.x2 or self.y1 == self.y2)


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int


@dataclass
class Board:
    called_coordinates: List[Coordinate] = field(default_factory=list)

    def log_line_coordinates(self, line: Line):
        for x in range(min(line.x1, line.x2), max(line.x1, line.x2) + 1):
            for y in range(min(line.y1, line.y2), max(line.y1, line.y2) + 1):
                self.called_coordinates.append(Coordinate(x, y))

    def number_overlapping_lines(self):
        counter = Counter(self.called_coordinates)
        return len([k for k, v in counter.items() if v > 1])


def get_input() -> List[Line]:
    with open("./input/day-5.txt") as f:
        contents = f.read().split("\n")
    lines = []
    for row in contents:
        x1, y1 = [int(x) for x in row.split("->")[0].split(",")]
        x2, y2 = [int(x) for x in row.split("->")[1].split(",")]
        lines.append(Line(x1, y1, x2, y2))
    return lines


def part_one(lines: List[Line]):
    board = Board()
    for line in lines:
        if line.is_horizontal_or_vertical:
            board.log_line_coordinates(line)

    return board.number_overlapping_lines()


if __name__ == "__main__":
    input = get_input()
    print(part_one(input))
