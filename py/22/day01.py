"""
    part_1: Every elf carry a quantity of calories, find the maximum amount of it | 66487
    part_2: Top 3 elf calories | 197301
"""


def helper(data):
    result = [sum(result) for result in data]
    result.sort(reverse=True)
    return result


def part_1(data):
    result = helper(data)
    result = result[:3]
    return result[0]


def part_2(data):
    result = helper(data)
    return sum(result[:3])
