from typing import Counter, List
import collections

def get_input() -> List[int]:
    with open("input/day-3.txt") as f:
        contents = f.read().split("\n")
    return [x for x in contents]


def part_one(input: List[int]):
    gamma_binary = ""
    for indx, _ in enumerate(input[0]):
        num_zero = 0
        num_one = 0
        
        for record in input:
            if int(record[indx]):
                num_one += 1
            else:
                num_zero += 1
        
        if num_zero >= num_one:
            gamma_binary += "0"
        else:
            gamma_binary += "1"
    
    gamma = int(gamma_binary, 2)
    epsilon = ((1 << len(gamma_binary)) - 1 - gamma)
    return gamma * epsilon

def find_oxygen_rating_for_position(input: List[int], position) -> int:
    position_values = [str(x)[position] for x in input]
    most_common = Counter(position_values).most_common(2)
    if len(most_common) == 1:
        return most_common[0][0]

    if most_common[0][1] == most_common[1][1]:
        return 1
    else:
        return most_common[0][0]

def find_co2_rating_for_position(input: List[int], position) -> int:
    position_values = [str(x)[position] for x in input]
    least_common = Counter(position_values).most_common()[::-1]

    if len(least_common) == 1:
        return least_common[0][0]
    
    if least_common[0][1] == least_common[1][1]:
        return 0
    else:
        return least_common[0][0]

def filter_input_by_pos_and_num(input: List[int], pos: int, num: int):
    return [x for x in input if str(x)[pos] == str(num)]
    
def find_oxygen_rating(input: List[int]):
    
    oxygen_input = input
    for indx, _ in enumerate(input[0]):
        most_common = find_oxygen_rating_for_position(oxygen_input, indx)
        oxygen_input = filter_input_by_pos_and_num(oxygen_input, indx, most_common)
        if len(oxygen_input) == 1:
            return(int(str(oxygen_input[0]), 2))

def find_co2_rating(input: List[int]):
    
    co2_rating = input
    for indx, _ in enumerate(input[0]):
        least_common = find_co2_rating_for_position(co2_rating, indx)
        co2_rating = filter_input_by_pos_and_num(co2_rating, indx, least_common)
        if len(co2_rating) == 1:
            return(int(str(co2_rating[0]), 2))


def part_two(input: List[int]):
    oxygen_rating = find_oxygen_rating(input)
    co2_rating = find_co2_rating(input) 
    return (oxygen_rating * co2_rating)

if __name__ == "__main__":
    input = get_input()
    print(part_one(input))
    print(part_two(input)) 