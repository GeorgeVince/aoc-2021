from dataclasses import dataclass
from typing import List
import itertools


@dataclass
class Board:
    rows: List[int]

    def is_low_point(self, x: int, y: int):
        adjacents = []

        for new_x, new_y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if y + new_y >= len(self.rows[x]) or y + new_y < 0:
                continue
            if x + new_x >= len(self.rows) or x + new_x < 0:
                continue
            adjacents.append(self.rows[x + new_x][y + new_y])

        if adjacents == []:
            return False

        return all([int(self.rows[x][y]) < int(adjacent) for adjacent in adjacents])


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


if __name__ == "__main__":
    input = get_input()
    print(part_one(input))
