from common.util import get_functions


def start_day():
    name = '--- Day 8: Treetop Tree House ---'
    parser_function = 'find_digits'
    display_lines_or_paragraph = 'lines'
    return name, parser_function, display_lines_or_paragraph


def helper(_data):
    return _data


def part_1(data):
    _data = helper(data)
    
    sum_items, add_together, Matrix2D, four_directions = get_functions(
        'sum_items', 'add_together', 'Matrix2D', 'four_directions'
    )

    def start_to_direction(start, direction, grid):
        while True:
            start = add_together(start, direction)
            if start not in grid:
                return
            yield start

    def visible_from_outside(grid) -> int:
        def is_visible(location) -> bool:
            return any(
                all(grid[point] < grid[location] for point in start_to_direction(location, direction, grid))
                for direction in four_directions
            )

        return sum_items(grid, is_visible)

    return visible_from_outside(Matrix2D(_data))
    

def part_2(data):
    return
