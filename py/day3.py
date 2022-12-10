#!/usr/bin/env python3
from util import get_input_str


def daily_input(day='day3'):
    return get_input_str(day)


def part_1(data):
    counter = 0
    
    for char in data:
        mid = len(char) // 2
        left = char[:mid]
        right = char[mid:]
    
        common, = set(left).intersection(right) 
        
        common = ord(common)
        char_a = ord('a') 
        char_A = ord('A')
        
        if common > char_a:
            counter += common - char_a + 1
        else:
            counter += common - char_A + 26 + 1
    
    return counter


def part_2(data):
    pass


def main(): 
    print(f'Part_1 is {part_1(daily_input())}.')  # 8053
    print(f'Part_2 is {part_2(daily_input())}.')  # todo
