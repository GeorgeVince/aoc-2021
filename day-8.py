from typing import List, Tuple


def get_input() -> List[Tuple[List[str], List[str]]]:
    with open("./input/day-8.txt", 'r') as f:
        contents = [x.replace("\n", "").split("|") for x in f.readlines()]
    return [(x[0].strip(), x[1].strip()) for x in contents]


def part_one(input: List[Tuple[List[str], List[str]]]) -> int:
    total = 0
    for _, output_value in input:
        # Count 1's
        parts = output_value.split(" ")
        total += sum(1 for x in parts if len(x) == 2)
        # Count 4's
        total += sum(1 for x in parts if len(x) == 4)
        # Count 7's
        total += sum(1 for x in parts if len(x) == 3)
        # Count 8's
        total += sum(1 for x in parts if len(x) == 7)
    return total


def part_two(input: List[Tuple[List[str], List[str]]]):
    total = 0

    for signal, output_value in input:
        signal_parts = ["".join(sorted(x)) for x in signal.split(" ")]
        output_parts = ["".join(sorted(x)) for x in output_value.split(" ")]

        patterns = {}

        patterns[1], = [x for x in signal_parts if len(x) == 2]
        patterns[4], = [x for x in signal_parts if len(x) == 4]
        patterns[7], = [x for x in signal_parts if len(x) == 3]
        patterns[8], = [x for x in signal_parts if len(x) == 7]

        patterns[3], = [x for x in signal_parts if len(
            x) == 5 and set(patterns[1]).issubset(x)]

        patterns[9], = [x for x in signal_parts if len(
            x) == 6 and set(patterns[4]).issubset(x)]

        patterns[5], = [x for x in signal_parts if len(
            x) == 5 and len(set(patterns[9]) - set(x)) == 1 and x != patterns[3]
        ]

        patterns[0], = [x for x in signal_parts if len(
            x) == 6 and set(patterns[7]).issubset(x) and x != patterns[9]
        ]

        patterns[2], = [x for x in signal_parts if len(
            x) == 5 and x not in patterns.values()
        ]

        patterns[6], = [x for x in signal_parts if len(
            x) == 6 and x not in patterns.values()
        ]

        patterns = dict(zip(patterns.values(), patterns.keys()))
        total += int("".join(str(patterns[part]) for part in output_parts))

    return total


if __name__ == "__main__":
    input = get_input()
    print(part_one(input))
    print(part_two(input))
