from src.common.utils import SolverFunctions
from collections import deque

title = '--- Day 8: Haunted Wasteland ---'
parser_method = 'strings_per_line'
handle_data = 'paragraph'  # by default


class SolveTheDay(SolverFunctions):    
    @classmethod
    def helper(cls, data):
        command, the_map = data
        command = command[0]
        mapped = {}
        
        for coord in the_map:
            key, values = coord.strip().split(' = ')
            left, right = values.replace('(', '').replace(')', '').replace(' ', '').split(',')
            mapped[key] = [left, right]

        counter = 0
        actual = 'AAA'

        while actual != 'ZZZ':
            counter += 1
            actual = mapped[actual][0 if command[0] == 'L' else 1]
            command = command[1:] + command[0]
    
        return counter
    
    @classmethod
    def level_1(cls, data):        
        return cls.helper(data)

    @classmethod
    def level_2(cls, data):
        data = cls.helper(data)
        
        return