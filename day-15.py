from queue import PriorityQueue


def dijkstra(
        weights,
        start,
        end) -> int:
    visited = set()
    lowest_weights = {}
    queue = PriorityQueue()
    queue.put((0, start))

    while not queue.empty():

        weight_from_start, pos = queue.get()
        if pos == end:
            # print(lowest_weights)
            return weight_from_start

        # update neighbor weights
        x, y = pos
        for neighbor in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if neighbor not in weights or neighbor in visited:
                continue

            new_weight = weight_from_start + weights[neighbor]
            old_weight = lowest_weights.get(neighbor)
            if old_weight and new_weight >= old_weight:
                continue

            # found a more efficient route
            lowest_weights[neighbor] = new_weight
            queue.put((new_weight, neighbor))

        visited.add(pos)
    


def get_input():
    with open('./input/day-15.txt', 'r') as f:
        contents = f.readlines()
    lines = [x.strip() for x in contents]
    return lines


def part_one(input) -> int:
    e = len(input) - 1

    weights = {
        (int(x), int(y)): int(weight)
        for y, line in enumerate(input)
        for x, weight in enumerate(line)
    }

    return dijkstra(
        weights=weights,
        start=(0, 0),
        end=(e, e),
    )


def part_two(input):
    weights = {
        (int(x), int(y)): int(weight)
        for y, line in enumerate(input)
        for x, weight in enumerate(line)
    }

    size = len(input)
    e = size * 5 - 1

    new_weights={
            (x + size * i, y + size * j): (weight - 1 + i + j) % 9 + 1
            for i in range(5)
            for j in range(5)
            for (x, y), weight in weights.items()
    }


    return dijkstra(
        weights=new_weights,
        start=(0, 0),
        end=(e, e),
    )



if __name__ == "__main__":
    input = get_input()
    print(part_one(input))
    print(part_two(input))
