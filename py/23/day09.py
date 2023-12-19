from src.common.utils import SolverFunctions

title = 'Day'
parser_method = 'strings_per_line'
handle_data = 'lines'  # by default


class SolveTheDay(SolverFunctions):    
    @classmethod
    def helper(cls, data, position):

        def extrapolate(array):
            if all(num == 0 for num in array):
                return 0

            differences = [x2 - x1 for x1, x2 in zip(array, array[1:])]
            if 'last' in position:
                return array[-1] + extrapolate(differences)

            if 'first' in position:
                diff = extrapolate(differences)
                return array[0] - diff
        
        total = 0

        for line in data:
            numbers = cls.integers(line[0])
            total += extrapolate(numbers)
        return total
    
    @classmethod
    def level_1(cls, data):
        return cls.helper(data, position='last')

    @classmethod
    def level_2(cls, data):
        return cls.helper(data, position='first')

