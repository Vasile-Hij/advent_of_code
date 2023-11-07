"""
    part_1: Every elf carry a quantity of calories, find the maximum amount of it | 66487
    part_2: Top 3 elf calories | 197301
"""


def start_day():
    name = '--- Day 1: Calorie Counting ---'
    parser_function = 'integers'
    display_lines_or_paragraph = 'paragraph'
    return name, parser_function, display_lines_or_paragraph


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
