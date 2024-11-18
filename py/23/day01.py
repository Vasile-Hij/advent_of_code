from src.common.utils import SolverFunctions
import re

title = '--- Day 1: Trebuchet?! ---'
parser_method = 'str_split'
visual_handler_data = 'paragraph'  # by default



class SolveTheDay(SolverFunctions):
    @classmethod
    def helper(cls, data):
        return cls.parse(data)

    @classmethod
    def level_1(cls, data):
        data = cls.helper(data)
        digits_data = [cls.find_digits(digit) for digit in data]

        result = 0
        for digits in digits_data:
            if len(digits) == 1:
                result += digits[0] + (10 * digits[0])

            if len(digits) == 2:
                result += (digits[0] * 10) + digits[1]

            if len(digits) > 2:
                result += (digits[0] * 10) + digits[-1]

        return result

    @classmethod
    def level_2(cls, data):
        _data = cls.helper(data)
        result = 0
        alpha_num = 'one two three four five six seven eight nine'.split()
        pattern = "(?=(" + "|".join(alpha_num) + "|\\d))"

        def get_position(num):
            if num in alpha_num:
                return str(alpha_num.index(num) + 1)
            return num

        for line in _data:
            digits = [*map(get_position, re.findall(pattern, line))]
            result += int(digits[0] + digits[-1])

        return result
