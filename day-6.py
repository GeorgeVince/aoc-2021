from dataclasses import dataclass
from typing import List


@dataclass
class LanternFish:
    time_left: int = 8
    first_cycle: bool = True

    def add_day(self):
        self.time_left -= 1
        if self.time_left < 0:
            self.time_left = 6
            self.first_cycle = False
            return LanternFish()


def get_input() -> int:
    with open("./input/day-6.txt", 'r') as f:
        contents = f.read()
    return [int(x) for x in contents.split(",")]

def simulate(inital_ages: List[int], num_days: int) -> int
    fishes = []
    num_days = 80

    for age in inital_ages:
        fishes.append(LanternFish(time_left=age, first_cycle=False))

    for _ in range(0, num_days):
        new_fishes = []
        for fish in fishes:
            new_fish = fish.add_day()
            if new_fish:
                new_fishes.append(new_fish)
        fishes.extend(new_fishes)
    return len(fishes)

def part_one(inital_ages: List[int]) -> int:
    return simulate(inital_ages, 80)



if __name__ == "__main__":
    input = get_input()
    print(part_one(input))
