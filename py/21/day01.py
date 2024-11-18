from src.common.utils import SolverFunctions

title = '--- Day 1: Sonar Sweep ---'
parser_method = ''
custom_parser_method = True
visual_handler_data = 'paragraph'  # by default


class SolveTheDay(SolverFunctions):
    @classmethod
    def helper(cls, data):
        return cls.get_each_line_split(data)

    @classmethod
    def level_1(cls, data):
        metrics = list(map(int, data))
        return sum([num_1 < num_2 for num_1, num_2 in zip(metrics, metrics[1:])])

    @classmethod
    def level_2(cls, data):
        metrics = list(map(int, data))
        pairs = list(zip(metrics, metrics[1:], metrics[2:]))
        return sum([sum(num_1) < sum(num_2) for num_1, num_2 in list(zip(pairs, pairs[1:]))])
