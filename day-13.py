def get_input():
    with open("./input/day-13.txt", 'r') as f:
        contents = f.readlines()
    
    coords = []
    folds = []
    for line in contents:
        if line.strip() and 'fold' not in line:
            split = line.strip().split(",")
            coords.append([int(split[0]), int(split[1])])
        elif "fold" in line:
            split = line.strip().split("=")
            folds.append([split[0][-1], int(split[1])])
    return coords, folds

def _fold(coord, fold):
    if fold[0] == "x":
            if coord[0] > fold[1]:
                coord[0] = fold[1] - (coord[0] - fold[1])
    if fold[0] == "y":
        if coord[1] > fold[1]:
            coord[1] = fold[1] - (coord[1] - fold[1])
    return coord
        

def part_one(coords, folds):
    for coord in coords:
        coord = _fold(coord, folds[0])
    
    return len (set([(*x,) for x in coords]))

def part_two(coords, folds):
    for fold in folds:
        for coord in coords:
            coord = _fold(coord, fold)
    
    return len (set([(*x,) for x in coords]))


if __name__ == "__main__":
    input = get_input()
    print(input)
    print(part_one(*input))
    print(part_two(*input))