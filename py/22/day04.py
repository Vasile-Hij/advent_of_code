from src.common.utils import SolverFunctions

title = 'Day 4: Camp Cleanup'
parser_method = 'str_strip'
display_lines_or_paragraph = 'lines'

#  find_range = lambda first, second: range(first, second + 1)  #  PEP8: E731


class SolveTheDay(SolverFunctions):
    @staticmethod
    def helper(first, second):
        return range(first, second + 1)

    @classmethod
    def part_1(cls, data):
        counter = 0
        for each_pair in data:
            first, second = each_pair.strip().split(',')
            first = set(cls.helper(*map(int, first.split('-'))))
            second = set(cls.helper(*map(int, second.split('-'))))
            # if len(first - second) == 0 or len(second - first) == 0:
            if first.issubset(second) or second.issubset(first):
                counter += 1
        return counter

    @classmethod
    def part_2(cls, data):
        counter = 0
        for each_pair in data:
            first, second = each_pair.strip().split(',')
            first = set(cls.helper(*map(int, first.split('-'))))
            second = set(cls.helper(*map(int, second.split('-'))))
            if len(first & second) > 0:
                counter += 1

        return counter
