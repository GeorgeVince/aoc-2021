from typing import List

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
    
   

if __name__ == "__main__":
    input = get_input()
    print(part_one(input))