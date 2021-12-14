from typing import List, Tuple
from collections import defaultdict

def get_input() -> List[Tuple[str, str]]:
    with open('./input/day-12.txt', 'r') as f:
        contents = [x.strip().split("-") for x in f.readlines()]
    return [(x[0], x[1]) for x in contents]

def part_one(input):
    caves = defaultdict(set)
    for row in input:
        caves[row[0]].add(row[1])
        caves[row[1]].add(row[0])
    
    start = [('start',)]
    paths = set()
    while start:
        path = start.pop()
        if path[-1] == 'end':
                paths.add(path)
                continue
        for node in caves[path[-1]]:
            if not node.islower() or node not in path:
                start.append((*path, node))
    
    return len(paths)
            



if __name__ == "__main__":
    input = get_input()
    print(part_one(input))
    