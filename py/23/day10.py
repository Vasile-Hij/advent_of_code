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
            direction = []
            for dx, dy in four_directions:
                for dxx, dyy in pipes[grid[x + dx][y + dy]]:
                    if dx + dxx == 0 and dy + dyy == 0:
                        direction.append((dx, dy))
            assert len(direction) == 2

            for char, moves in pipes.items():
                if all(move in moves for move in direction):
                    return char

        def get_valid_moves(x, y):
            pipe_type = grid[x][y]
            return [(x + dx, y + dy) for dx, dy in pipes[pipe_type]]

        grid[start_row] = grid[start_row].replace('S', get_starting_point(start_row, start_col))

        x, y = start_row, start_col
        queue = deque([(x, y)])

        while queue:  # BFS
            x, y = queue.popleft()

            if (x, y) in seen:
                continue
            seen.add((x, y))

            for row, col in get_valid_moves(x, y):
                queue.append((row, col))

        return grid, seen

    @classmethod
    def level_1(cls, data):
        _, seen = cls.helper(data)
        return len(seen) // 2

    @classmethod
    def level_2(cls, data):
        grid, seen = cls.helper(data)

        new_grid = ''
        for row, line in enumerate(grid):
            for col, elem in enumerate(line):
                new_grid += '.' if (row, col) not in seen else elem
            new_grid += '\n'

        new_grid = new_grid.split('\n')

        counter = 0
        for elem in new_grid:
            outside = True
            start_F = None
            for el in elem:
                match el:
                    case '.':
                        if not outside:
                            counter += 1
                    case '|':
                        outside = not outside
                    case 'F':
                        start_F = True
                    case 'L':
                        start_F = False
                    case '-':
                        assert start_F is not None
                    case '7':
                        assert start_F is not None
                        if not start_F:
                            outside = not outside
                        start_F = None
                    case 'J':
                        assert start_F is not None
                        if start_F:
                            outside = not outside
                        start_F = None

        return counter
