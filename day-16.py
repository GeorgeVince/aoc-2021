from dataclasses import dataclass, field
from functools import reduce

@dataclass
class Packet:
    version: int
    type_id: int
    value: int
    sub_packets: field(default_factory=list)


def get_input():
    with open('./input/day-16.txt') as file:
        return [hex_to_bin(line) for line in file.read().splitlines()]


def hex_to_bin(hex_str):
    return bin(int(hex_str, 16))[2:].zfill(len(hex_str) * 4)


def decode(transmission, i):
    version = int(transmission[i:(i + 3)], 2)
    type_id = int(transmission[(i + 3):(i + 6)], 2)
    i += 6
    if type_id == 4:
        value, i = get_literal_value(transmission, i)
        return Packet(version, type_id, value, []), i
    length_type_id = transmission[i]
    i += 1
    if length_type_id == "0":
        sub_packets, i = get_sub_packets_by_length(transmission, i)
    else:
        sub_packets, i = get_sub_packets_by_number(transmission, i)
    value = calculate_value(type_id, sub_packets)
    return Packet(version, type_id, value, sub_packets), i


def get_literal_value(transmission, i):
    value = ""
    while True:
        last_group = transmission[i] == "0"
        value += transmission[(i + 1):(i + 5)]
        i += 5
        if last_group:
            break
    return int(value, 2), i


def get_sub_packets_by_length(transmission, i):
    sub_packets = []
    length_of_sub_packets = int(transmission[i:(i + 15)], 2)
    i += 15
    length_used = 0
    while length_used < length_of_sub_packets:
        sub_packet, new_i = decode(transmission, i)
        sub_packets.append(sub_packet)
        length_used += new_i - i
        i = new_i
    return sub_packets, i

def calculate_value(type_id, sub_packets):
    value = 0
    if type_id <= 3:
        values = (sub_packet.value for sub_packet in sub_packets)
        if type_id == 0:
            value = sum(values)
        elif type_id == 1:
            value = reduce((lambda x, y: x * y), values)
        elif type_id == 2:
            value = min(values)
        elif type_id == 3:
            value = max(values)
    else:
        sub_a, sub_b = sub_packets
        if type_id == 5:
            value = sub_a.value > sub_b.value
        elif type_id == 6:
            value = sub_a.value < sub_b.value
        elif type_id == 7:
            value = sub_a.value == sub_b.value
        value = int(value)
    return value

def get_sub_packets_by_number(transmission, i):
    sub_packets = []
    number_of_sub_packets = int(transmission[i:(i + 11)], 2)
    i += 11
    for _ in range(number_of_sub_packets):
        sub_packet, i = decode(transmission, i)
        sub_packets.append(sub_packet)
    return sub_packets, i


def sum_versions(packet):
    total = packet.version
    for sub_packet in packet.sub_packets:
        total += sum_versions(sub_packet)
    return total


def part_one(transmission):
    outer_packet = decode(transmission[0], 0)[0]
    return sum_versions(outer_packet)

def part_two(transmission):
    outer_packet = decode(transmission[0], 0)[0]
    return outer_packet.value

if __name__ == "__main__":
    input = get_input()
    print(part_one(input))
    print(part_two(input))