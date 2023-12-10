from functools import cache

from src.common.utils import SolverFunctions

title = '--- Day 5: If You Give A Seed A Fertilizer ---'
parser_method = 'strings_per_line'
display_lines_or_paragraph = 'paragraph'  # by default


class SolveTheDay(SolverFunctions):    
    @classmethod
    def helper(cls, data):
        return
    
    @classmethod
    def level_1(cls, data):
        seeds, *blocks = cls.each_item(data)
        
        raw_seeds = [x.strip() for x in seeds[0].split(':')][1]
        seeds = [int(x) for x in raw_seeds.split(' ')]

        blocks = [block[1:] for block in blocks]


        @cache
        def follow(value):
            directions = []
            for block in blocks:
                
                for position, positions in enumerate(block):

                    destination, source, length = [int(x) for x in positions.split()]
                    if source <= value < source + length:
                        value = destination + (value - source)
                        directions.append(position)
                        break
                else:
                    directions.append(None)
            return value, directions
        
        return list(min(list(map(follow, seeds))))[0]

    @classmethod
    def level_2(cls, data):
        data = cls.helper(data)
        
        return