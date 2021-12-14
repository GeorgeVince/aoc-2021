from typing import List


pair_score = {'()': 3, '[]': 57,
              '{}': 1197, '<>': 25137}


def get_input():
    with open('./input/day-10.txt', 'r') as f:
        contents = f.readlines()
    return [x.strip() for x in contents]


def part_one(input: List[str]) -> int:
    left_pair = [x[0] for x in pair_score.keys()]
    right_pair = [x[1] for x in pair_score.keys()]
    points = 0
    for row in input:
        stack = []
        for char in row:
            if char in left_pair:
                stack.append(char)
            else:
                try:
                    popped = stack.pop()
                except IndexError:
                    popped = None
                combined = popped + char
                if combined not in pair_score:
                    points += list(pair_score.values())[right_pair.index(char)]
                    break
    return points

def part_two(input: List[str]) -> int:
    stack = []
    left_pair = [x[0] for x in pair_score.keys()]
    right_pair = [x[1] for x in pair_score.keys()]
    points = 0
    for row in input:
        for char in row:
            if char in left_pair:
                stack.append(char)
            else:
                try:
                    popped = stack.pop()
                except IndexError:
                    popped = None
                combined = popped + char
                if combined not in pair_score:
                    break
            
    return points


if __name__ == "__main__":
    input = get_input()
    print(part_one(input))
