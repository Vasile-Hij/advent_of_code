"""
    part_1: Every elf carry a quantity of calories, find the maximum amount of it | 66487
    part_2: Top 3 elf calories | 197301
"""
from src.common.utils import SolverFunctions

title = 'Day 1: Calorie Counting'
parser_method = 'integers'
handle_data = 'paragraph'


class SolveTheDay(SolverFunctions):    
    @staticmethod
    def helper(data):
        result = [sum(result) for result in data]
        result.sort(reverse=True)
        return result
    
    @classmethod
    def level_1(cls, data):
        result = cls.helper(data)
        result = result[:3]
        return result[0]

    @classmethod
    def level_2(cls, data):
        result = cls.helper(data)
        return sum(result[:3])
