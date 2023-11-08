from src.common.utils import SolverFunctions

title = 'Day 6: Tuning Trouble'
parser_method = 'str_strip'
display_lines_or_paragraph = 'lines'


class SolveTheDay(SolverFunctions):    
    @staticmethod
    def helper(data, stream_buffer):
        _data = data[0]
        for index, _ in enumerate(_data):
            if len(set(_data[index - stream_buffer: index])) == stream_buffer:
                return index

    @classmethod
    def part_1(cls, data):
        message = cls.helper(data, 4)
        return message

    @classmethod
    def part_2(cls, data):
        message = cls.helper(data, 14)
        return message
