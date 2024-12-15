from src.common.utils import SolverFunctions
import re

title = '--- Day 3: Mull It Over ---'
parser_method = ''
custom_parser_method = True  # if True no parser method is required!!!
visual_handler_data = 'paragraph'  # by default


class SolveTheDay(SolverFunctions):
    @classmethod
    def helper(cls, data):
        return cls.str_strip(data)

    @classmethod
    def level_1(cls, data):
        return cls.calculations(data)

    @classmethod
    def level_2(cls, data):
        is_enabled = True
        result = 0

        matches = re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", data)

        for string in matches:
            if string == "do()":
                is_enabled = True
            elif string == "don't()":
                is_enabled = False
            elif string.startswith("mul") and is_enabled:
                result += cls._product(cls.integers(cls.numbers(string)[0]))

        return result

    @classmethod
    def calculations(cls, strings):
        return sum([cls._product(cls.integers(nums)) for nums in cls.numbers(strings)])

    @classmethod
    def numbers(cls, strings):
        return re.findall(r'mul\(\d+,\d+\)', strings)
