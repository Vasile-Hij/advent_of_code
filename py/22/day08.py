from src.common.utils import SolverFunctions, Matrix2D, four_directions
title = 'Day 8: Treetop Tree House'
parser_method = 'find_digits'
display_lines_or_paragraph = 'lines'


class SolveTheDay(SolverFunctions, Matrix2D):
    @classmethod
    def helper(cls, _data):
        def start_to_direction(start, direction, grid):
            while True:
                start = cls.add_together(start, direction)
                if start not in grid:
                    return
                yield start
  
        return _data, start_to_direction

    @classmethod
    def level_1(cls, data):
        _data, start_to_direction = cls.helper(data)

        def visible_from_outside(grid) -> int:
            def is_visible(location) -> bool:
                return any(
                    all(grid[point] < grid[location] for point in start_to_direction(location, direction, grid))
                    for direction in four_directions
                )
    
            return cls.sum_items(grid, is_visible)
    
        return visible_from_outside(Matrix2D(_data))

    @classmethod
    def level_2(cls, data):
        _data, start_to_direction = cls.helper(data)
        
        def distance_result(location, grid):
            return cls._product(visual_distance(location, direction, matrix) for direction in four_directions)
                
        def visual_distance(location, direction, grid):
            seen = 0
            
            for seen, point in enumerate(start_to_direction(location, direction, matrix), 1):
                if matrix[point] >= matrix[location]:
                    break
            return seen
                    
        matrix = Matrix2D(grid=_data)
        
        return max(distance_result(point, matrix) for point in matrix)
