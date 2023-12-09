from src.common.utils import SolverFunctions
from more_itertools import locate

title = '--- Day 4: Scratchcards ---'
parser_method = 'strings_per_line'
display_lines_or_paragraph = 'paragraph'  # by default


class SolveTheDay(SolverFunctions):    
    @classmethod
    def helper(cls, data, level=None):
        data = cls.parse(data)

        pile_scratchcards = []
        cards = {}

        for position, line in enumerate(data):
            _, sets = line.split(':'.strip())
            set_1, set_2 = sets.split('|')
            list_1, list_2 = cls.integers(set_1), cls.integers(set_2)

            common = len(set(list_1).intersection(list_2))

            if level == 1:
                times_occurred = 1 if common == 1 \
                    else [1, *(cls.range_generator(number=common, start=1, multiplier=2))] \
                    if common > 1 else 0

                if isinstance(times_occurred, list):
                    times_occurred = cls._product(times_occurred)

                pile_scratchcards.append(times_occurred)
                
            if level == 2:
                if position not in cards.keys():
                    cards[position] = 1
                
                if common:
                    for num in range(position + 1, position + common + 1):
                        cards[num] = cards.get(num, 1) + cards[position]

        return sum(pile_scratchcards) if level == 1 else sum(cards.values())

    @classmethod
    def level_1(cls, data):
        return cls.helper(data, level=1)

    @classmethod
    def level_2(cls, data):
        return cls.helper(data, level=2)
