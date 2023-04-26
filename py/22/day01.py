"""
    part_1: Every elf carry a quantity of calories, find the maximum amount of it | 66487
    part_2: Top 3 elf calories | 197301
"""
from common.util import get_data_num


def daily_input(year='22', day='01', separator_two='\n\n'):
    return get_data_num(year, day, separator_two)


def part_1(data):
    top = [sum(result) for result in data]
    # return max(top), top
    top.sort(reverse=True)
    return top[:3]


def part_2(data):
    # data.sort(reverse=True)
    # return sum(data[:3])
    return sum(data)


def main():
    print(f'Part_1 is {part_1(data=daily_input())[0]}.')
    print(f'Part_2 is {part_2(data=part_1(daily_input()))}.')  # data=part_1(daily_input()[1]


if __name__ == '__main__':
    main()
