from src.common.utils import SolverFunctions

title = '--- Day 4: Scratchcards ---'
parser_method = 'strings_per_line'
display_lines_or_paragraph = 'paragraph'  # by default


class SolveTheDay(SolverFunctions):    
    @classmethod
    def helper(cls, data):
        data = cls.parse(data)
        pile_scratchcards = []
        
        for position, line in enumerate(data):
            _, sets = line.split(':'.strip())
            set_1, set_2 = sets.split('|')
            set_1, set_2 = cls.integers(set_1), cls.integers(set_2)

            common = set(set_1).intersection(set_2)
            length = len(common)

            times_occurred = 1 if length == 1 \
                else [1, *(cls.range_generator(number=length, start=1, multiplier=2))] \
                if length > 1 else 0

            if isinstance(times_occurred, list):
                times_occurred = cls._product(times_occurred)

            pile_scratchcards.append(times_occurred)
        
        return sum(pile_scratchcards)
    
    @classmethod
    def level_1(cls, data):
        result = cls.helper(data)
        
        return result

    @classmethod
    def level_2(cls, data):
        result = cls.helper(data)
        
        return