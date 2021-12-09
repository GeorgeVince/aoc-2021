from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class Board:
    rows: List[List[int]] = field(default_factory=list)
    called: List[List[int]] = field(default_factory=list)

    def is_winner(self):
        target_row = len(self.rows[0])
        target_col = len(self.rows)

        # Check for rows
        for row in self.called:
            if sum(row) == target_row:
                return True

        # Check for cols
        for indx, _ in enumerate(self.called[0]):
            col = [row[indx] for row in self.called]
            if sum(col) == target_col:
                return True

        return False

    def mark_number(self, number):
        for row, _ in enumerate(self.rows):
            for col, _ in enumerate(self.rows[0]):
                if self.rows[row][col] == number:
                    self.called[row][col] = 1
                    return

    def sum_unmarked(self):
        total = 0
        for row, _ in enumerate(self.rows):
            for col, _ in enumerate(self.rows[0]):
                if not self.called[row][col]:
                    total += self.rows[row][col]
        return total


def get_input() -> Tuple[List[int], List[Board]]:
    with open("./input/day-4.txt", 'r') as f:
        content = f.readlines()

    bingo_numbers = []
    boards = []
    board = Board()
    for indx, row in enumerate(content):
        if indx == 0:
            bingo_numbers = [int(x) for x in row.split(",") if x.isdigit()]
            continue
        if row == "\n":
            if board.rows:
                boards.append(board)
            board = Board()
            continue
        board.rows.append([int(x) for x in row.split() if x.isdigit()])
        board.called.append([0 for x in row.split() if x.isdigit()])

    boards.append(board)
    return bingo_numbers, boards


def part_one(bingo_numbers: List[int], boards: List[Board]) -> int:
    for num in bingo_numbers:
        for board in boards:
            board.mark_number(num)
            if board.is_winner():
                return board.sum_unmarked() * num

def part_two(bingo_numbers: List[int], boards: List[Board]) -> int:
    won_boards = []
    for num in bingo_numbers:
        for board in boards:
            if board in won_boards:
                continue
            board.mark_number(num)
            if board.is_winner():
                if len(won_boards) == len(boards) - 1:
                     return board.sum_unmarked() * num
                won_boards.append(board)
    


if __name__ == "__main__":
    bingo_numbers, boards = get_input()
    print(part_one(bingo_numbers, boards))
    print(part_two(bingo_numbers, boards))
