from src.common.utils import SolverFunctions

title = '--- Day 2: Dive! ---'
parser_method = ''
custom_parser_method = True
visual_handler_data = 'paragraph'  # by default


class SolveTheDay(SolverFunctions):
    @classmethod
    def helper(cls, data):
        return cls.get_each_line_split(data)

    @classmethod
    def level_1(cls, data):
        position = depth = 0

        for instructions in data:
            direction, num = instructions.split()
            num = int(num)
            if direction == 'forward':
                position += num
            if direction == 'down':
                depth += num
            if direction == 'up':
                depth -= num

        return position * depth

    @classmethod
    def level_2(cls, data):
        position = depth = aim = 0

        for instructions in data:
            direction, num = instructions.split()
            num = int(num)
            if direction == 'forward':
                position += num
                depth += aim * num
            if direction == 'down':
                aim += num
            if direction == 'up':
                aim -= num
        return position * depth
