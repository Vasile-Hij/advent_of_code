from functools import cache

from src.common.utils import SolverFunctions

title = '--- Day 5: If You Give A Seed A Fertilizer ---'
parser_method = 'strings_per_line'
display_lines_or_paragraph = 'paragraph'  # by default


class SolveTheDay(SolverFunctions):    
    @classmethod
    def helper(cls, data):
        raw_seeds, *blocks = cls.each_item(data)

        raw_seeds = [x.strip() for x in raw_seeds[0].split(':')][1]
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

        return seeds, blocks, follow

    @classmethod
    def level_1(cls, data):
        seeds, blocks, follow = cls.helper(data)
        return list(min(list(map(follow, seeds))))[0]

    @classmethod
    def level_2(cls, data):
        seeds, blocks, follow = cls.helper(data)
        result = 10**100

        def binary_search(start, end):
            mid = (start + end) // 2
            val_start = follow(start)
            val_end = follow(end)
            
            if val_start[1] == val_end[1]:
                return val_start[0]

            if end == start + 1:
                return min(val_start[0], val_end[0])

            return min(binary_search(start, mid), binary_search(mid, end))

        for position in range(0, len(seeds), 2):
            start, length = seeds[position], seeds[position + 1]
            results = binary_search(start, start + length - 1)
            result = min(result, results)

        return result
