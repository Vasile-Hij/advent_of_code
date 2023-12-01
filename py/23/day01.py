from src.common.utils import SolverFunctions

title = 'Day'
parser_method = 'str_split'
display_lines_or_paragraph = 'paragraph'  # by default


class SolveTheDay(SolverFunctions):    
    @classmethod
    def helper(cls, data):
        return cls.parse(data)
    
    @classmethod
    def part_1(cls, data):
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
    def part_2(cls, data):
        digits_data = cls.helper(data)
        
        return