from src.common.utils import SolverFunctions
from typing import List

title = '--- Day 2: Red-Nosed Reports ---'
parser_method = ''
custom_parser_method = True  # if True no parser method is required!!!
visual_handler_data = 'paragraph'  # by default


class SolveTheDay(SolverFunctions):
    @classmethod
    def helper(cls, data):
        return cls.all_atoms(data)

    @classmethod
    def level_1(cls, data):
        return sum(map(cls.strict, data))

    @classmethod
    def level_2(cls, data):
        return sum(map(cls.tolerance, data))

    @classmethod
    def strict(cls, elem) -> bool:
        check = {elem[x] - elem[x - 1] for x in range(1, len(elem))}
        return check.issubset({1, 2, 3}) or check.issubset({-1, -2, -3})

    @classmethod
    def tolerance(cls, elem) -> bool:
        data = cls.one_broken(elem)
        return any(map(cls.strict, data))

    def one_broken(elem) -> List:
        return (elem[:x] + elem[x + 1:] for x in range(len(elem)))
