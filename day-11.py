from dataclasses import dataclass, field
from typing import List, Tuple
import itertools


@dataclass
class Board:
    rows: List[List[int]]

    def simulate(self, turns: int):
        total_flashes = 0
        for _ in range(0, turns):
            flashed = []
            for x, _ in enumerate(self.rows):
                for y, _ in enumerate(self.rows[x]):
                    new_flashes = self._simulate_tile(x, y, flashed)
                    flashed.extend(new_flashes)
            total_flashes += len(flashed)
        return total_flashes

    def simulate_part_two(self):
        all_flashes = sum(sum([1 for x in row]) for row in self.rows)

        flashed = []
        for x, _ in enumerate(self.rows):
            for y, _ in enumerate(self.rows[x]):
                new_flashes = self._simulate_tile(x, y, flashed)
                flashed.extend(new_flashes)
        turn_flashed = len(flashed)
        return turn_flashed == all_flashes


    def _simulate_tile(self, x, y, flashed):
        to_check = [(x, y)]
        new_flashes = []
        while to_check:
            x, y = to_check.pop()
            
            if (x, y) in flashed or (x, y) in new_flashes: 
                    continue

            self.rows[x][y] += 1

            if self.rows[x][y] > 9:
                new_flashes.append((x, y))
                to_check.extend(self._find_neighbours(x, y))
                self.rows[x][y] = 0

        return new_flashes

    def _find_neighbours(self, x, y) -> List[Tuple]:
        neighbours = []
        for offset_x, offset_y in set(itertools.permutations(list(range(-1, 2)) * 2, 2)):
            new_x = x + offset_x
            new_y = y + offset_y
            if (new_x, new_y) == (x, y):
                continue
            if not self._is_valid_position(new_x, new_y):
                continue
            neighbours.append((new_x, new_y))
        return neighbours

    def _is_valid_position(self, x, y) -> bool:
        if x >= len(self.rows) or x < 0:
            return False
        if y >= len(self.rows[x]) or y < 0:
            return False
        return True


def get_input() -> Board:
    with open('./input/day-11.txt', 'r') as f:
        contents = f.readlines()
    return Board(rows=[[int(x) for x in line.strip()] for line in contents])

def part_one(board: Board):
    return board.simulate(100)

def part_two(board: Board):
    start_turn = 1
    while not board.simulate_part_two():
        start_turn += 1
    return start_turn



if __name__ == "__main__":
    input = get_input()
    print(part_one(input))

    input = get_input()
    print(part_two(input))
