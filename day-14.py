from collections import Counter

def get_input():
    with open('./input/day-14.txt', 'r') as f:
        contents = [x.strip() for x in f.readlines()]
    template = contents[0]

    rules = {x.split("->")[0].strip(): x.split("->")[1].strip()
             for x in contents[2:]}

    return template, rules


def part_one(template, rules):
    num_steps = 10

    polymer = list(template)
    for _ in range(0, num_steps):
        tmp = ""
        for indx, _ in enumerate(polymer[:-1]):
            tmp += polymer[indx]
            tmp += rules["".join(polymer[indx:indx+2])]
        polymer = tmp + polymer[-1]

    c = Counter(polymer)
    return c.most_common()[0][1] - c.most_common()[-1][1]




if __name__ == "__main__":
    input = get_input()
    print(part_one(*input))
    #print(part_two(*input))
