from src.common.utils import SolverFunctions
import re

title = '--- Day 3: Mull It Over ---'
parser_method = 'str_strip'
custom_parser_method = False  # if True no parser method is required!!!
visual_handler_data = 'paragraph'  # by default


class SolveTheDay(SolverFunctions):
    @classmethod
    def helper(cls, data):
        return cls.concat(data)

    @classmethod
    def level_1(cls, data):
        return cls.calculations(data[0])

    @classmethod
    def level_2(cls, data):
        return cls.calculations(cls.exclude(data[0]))

    @classmethod
    def calculations(cls, strings):
        return sum([cls._product(cls.integers(nums)) for nums in cls.numbers(strings)])

    @classmethod
    def numbers(cls, strings):
        return re.findall(r'mul\(\d+,\d+\)', strings)

    @classmethod
    def exclude(cls, strings):
        return re.sub(r"don't\(\).*?(do\(\)|$)", ' ', strings)
