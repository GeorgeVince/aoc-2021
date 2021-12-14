from dataclasses import dataclass, field
from typing import List, Tuple
import math


@dataclass
class Board:
    rows: List[int]
    checked: List[Tuple] = field(default_factory=list)
    basin_sizes: List[int] = field(default_factory=list)

    def is_low_point(self, x: int, y: int) -> bool:
        adjacents = []

        for new_x, new_y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if not self._is_valid_position(x + new_x, y + new_y):
                continue
            adjacents.append(self.rows[x + new_x][y + new_y])

        if adjacents == []:
            return False

        return all([int(self.rows[x][y]) < int(adjacent) for adjacent in adjacents])

    def _is_valid_position(self, x, y) -> bool:
        if x >= len(self.rows) or x < 0:
            return False
        if y >= len(self.rows[x]) or y < 0:
            return False
        return True

    def find_basin(self, x: int, y: int) -> bool:
        # Exit early if already checked or not a basin.
        if (x, y) in self.checked:
            return False

        if int(self.rows[x][y]) == 9:
            return False

        to_check = [(x, y)]
        basin_size = 0
        while to_check:
            x, y = to_check.pop()
            for offset_x, offset_y in [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_x = x + offset_x
                new_y = y + offset_y
                if not self._is_valid_position(new_x, new_y):
                    continue
                if (new_x, new_y) in self.checked:
                    continue
                if int(self.rows[new_x][new_y]) == 9:
                    continue

                if (new_x, new_y) not in self.checked:
                    basin_size += 1
                    self.checked.append((new_x, new_y))

                if (new_x, new_y) not in to_check and (offset_x, offset_y) != (0, 0):
                    to_check.append((new_x, new_y))

        self.basin_sizes.append(basin_size)
        return True


def get_input() -> Board:
    with open('./input/day-9.txt', 'r') as f:
        contents = f.readlines()
    return Board(rows=[line.strip() for line in contents])


def part_one(board: Board):
    low_points = []
    for x, row in enumerate(board.rows):
        for y, _ in enumerate(row):
            if board.is_low_point(x, y):
                low_points.append(int(board.rows[x][y]))
    return sum([height + 1 for height in low_points])


def part_two(board: Board):
    for x, row in enumerate(board.rows):
        for y, _ in enumerate(row):
            board.find_basin(x, y)

    return math.prod(sorted(board.basin_sizes)[-3:])


if __name__ == "__main__":
    input = get_input()
    print(part_one(input))
    print(part_two(input))
