from dataclasses import dataclass
from math import inf


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



def valid_path(start_coordinate, target):
    coords = [Coordinate(0, 0)]
    x, y = start_coordinate.x, start_coordinate.y
    rel_x, rel_y = x, y
    
    while rel_y >= target.y1:
        if x > 0:
            x -= 1
        y -= 1
        coords.append(Coordinate(rel_x, rel_y))
        rel_x = rel_x + x
        rel_y = rel_y + y

    return any(in_target(coord, target) for coord in coords[::-1])

def calculate_loc(start_coordinate):
    x, y = start_coordinate.x, start_coordinate.y
    rel_x, rel_y = x, y
    points = [Coordinate(0, 0)]
    while y > 0:
        if x > 0:
            x -= 1
        y -= 1
        points.append(Coordinate(rel_x, rel_y))
        rel_x = rel_x + x
        rel_y = rel_y + y
    
    return points[-1]
        
        


def in_target(coord: Coordinate, target: TargetArea):
    return (coord.x >= target.x1
            and coord.x <= target.x2
            and coord.y >= target.y1
            and coord.y <= target.y2)


def optimise(target):
    # Step 1 horiztonal velocity
    x, y = 0, 0
    possible_x = []
    while True:
        coord = Coordinate(x, y)
        if valid_path(coord, target):
            possible_x.append(coord)
        else:
            # we have found our last possible
            if possible_x:
                break
        x += 1

    # Brute for Y positions
    max_y_loc = -inf
    for coord in possible_x:
        x, y = coord.x, coord.y
        while y < 1000:
            if valid_path(Coordinate(x, y), target):
                y_loc = calculate_loc(Coordinate(x, y)).y
                max_y_loc = max(y_loc, max_y_loc)
            y += 1
            
    
    return max_y_loc

def part_one(input):
    target = parse_target(input)
    return(optimise(target))

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
    print(part_one(input))
