from typing import List
from dataclasses import dataclass


@dataclass
class Instruction:
    direction: str
    amount: int


@dataclass
class Coordinates:
    horizontal: int = 0
    depth: int = 0
    aim: int = 0


def get_input() -> List[Instruction]:
    with open("input/day-2.txt") as f:
        contents = f.readlines()

    return [
        Instruction(direction=line.split()[0], amount=int(line.split()[1]))
        for line in contents
    ]


def adjust_coordinates(
    instruction: Instruction, coordinates: Coordinates
) -> Coordinates:
    if instruction.direction == "forward":
        coordinates.horizontal += instruction.amount
    if instruction.direction == "up":
        coordinates.depth -= instruction.amount
    if instruction.direction == "down":
        coordinates.depth += instruction.amount
    return coordinates


def adjust_coordinates_and_aim(
    instruction: Instruction, coordinates: Coordinates
) -> Coordinates:
    if instruction.direction == "forward":
        coordinates.horizontal += instruction.amount
        coordinates.depth += (coordinates.aim * instruction.amount)
    if instruction.direction == "up":
        coordinates.aim -= instruction.amount
    if instruction.direction == "down":
        coordinates.aim += instruction.amount
    return coordinates


def step_one(instructions: List[Instruction]) -> int:
    coordinates = Coordinates()
    for instruction in instructions:
        coordinates = adjust_coordinates(instruction, coordinates)
    return coordinates.horizontal * coordinates.depth


def step_two(instructions: List[Instruction]) -> int:
    coordinates = Coordinates()
    for instruction in instructions:
        coordinates = adjust_coordinates_and_aim(instruction, coordinates)
    return coordinates.horizontal * coordinates.depth


if __name__ == "__main__":
    input = get_input()
    print(step_one(input))
    print(step_two(input))
