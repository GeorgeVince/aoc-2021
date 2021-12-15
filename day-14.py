from collections import Counter, defaultdict


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


def part_two(template, rules):
    chunks = [template[i:i+2]
              for i in range(0, len(template) - 1)]
    num_steps = 40

    c = Counter(chunks)
    for turn in range(0, num_steps):

        for k, v in c.copy().items():
            if v >= 1:
                c[k] = c[k] - v
                new_key_left = k[0] + rules[k]
                new_key_right = rules[k] + k[1]
                c[new_key_left] += v
                if turn != num_steps - 1:
                    c[new_key_right] += v

    total_count = defaultdict(int)
    for k, v in c.items():
        total_count[k[0]] += v
        total_count[k[1]] += v

    total_count[template[-1]] += 1

    return max(v for v in total_count.values()) - min(v for v in total_count.values())


if __name__ == "__main__":
    input = get_input()
    print(part_one(*input))
    print(part_two(*input))
