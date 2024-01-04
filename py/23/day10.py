from src.common.utils import (
    SolverFunctions, four_directions, East, South, West, North
)
from collections import deque

title = '--- Day 10: Pipe Maze ---'
parser_method = 'str_strip'
handle_data = 'lines'  # by default


class SolveTheDay(SolverFunctions):    
    @classmethod
    def helper(cls, data):
        return
    
    @classmethod
    def level_1(cls, data):
        grid = list(data)
        seen = set()
        start_row, start_col = None, None
        
        pipes = {
            '|': (East, West),
            '-': (South, North),
            'L': (West, South),
            'J': (West, North),
            '7': (East, North),
            'F': (East, South),
            '.': (),
        }

        for start_row, line in enumerate(grid):
            try:
                start_col = line.index('S')
                break
            except ValueError:
                pass

        def get_starting_point(x, y):
            res = []
            for dx, dy in four_directions:
                for dxx, dyy in pipes[grid[x + dx][y + dy]]:
                    print(x, y, dx, dy, dxx, dyy)
                    if dx + dxx == 0 and dy + dyy == 0:
                        print(dx, dy)
                        res.append((dx, dy))
            assert len(res) == 2
            
            for char, moves in pipes.items():
                if all(move in moves for move in res):
                    return char
        
        def get_valid_moves(x, y):
            pipe_type = grid[x][y]
            return [(x + dx, y + dy) for dx, dy in pipes[pipe_type]]
        
        grid[start_row] = grid[start_row].replace('S', get_starting_point(start_row, start_col))

        x, y = start_row, start_col
        queue = deque([(x, y)])
        
        while queue:
            x, y = queue.popleft()
            
            if (x, y) in seen:
                continue
            seen.add((x, y))
        
            for row, col in get_valid_moves(x, y):
                queue.append((row, col))
        
        return len(seen) // 2
        


    @classmethod
    def level_2(cls, data):
        data = cls.helper(data)
        
        return