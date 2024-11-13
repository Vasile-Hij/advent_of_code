from src.common.utils import SolverFunctions

title = '--- Day 1: Sonar Sweep ---'
parser_method = 'str_split'
handle_data = 'paragraph'  # by default


class SolveTheDay(SolverFunctions):
    @classmethod
    def helper(cls, data):
        return cls.parse(data)

    @classmethod
    def level_1(cls, data):
        # tmp = None
        # counter = 0

        # for num in list(map(int, cls.helper(data))):
        #     if not tmp:
        #         tmp = num
        #         continue

        #     if tmp < num:
        #         counter += 1
        #         tmp = num
        #         continue

        #     if tmp > num:
        #         tmp = num
        #         continue
            
        # second version
        metrics = list(map(int, cls.helper(data)))
        return sum([num_1 < num_2 for num_1, num_2 in zip(metrics, metrics[1:])])

    @classmethod
    def level_2(cls, data):
        metrics = list(map(int, cls.helper(data)))
        pairs = list(zip(metrics, metrics[1:], metrics[2:]))
        return sum([sum(num_1) < sum(num_2) for num_1, num_2 in list(zip(pairs, pairs[1:]))])
