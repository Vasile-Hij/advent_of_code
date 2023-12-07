from src.common.utils import SolverFunctions, Matrix2D, eight_directions
import collections

title = '--- Day 3: Gear Ratios ---'
parser_method = 'strings_per_line'
display_lines_or_paragraph = 'paragraph'  # by default


class SolveTheDay(SolverFunctions):    
    @classmethod
    def helper(cls, data):
        grid = cls.parse(data)

        grid_numbers = {}
        validators = {}
        gears = {}
        counter = 0
        validator_counter = 0
        gears_counter = 0
        
        def update_number(number_counter, num, pos_x, start_num, pos_y):
            grid_numbers.update({number_counter: [num, pos_x, start_num, pos_y - 1]})
            number_counter += 1
            start_num, num = 0, 0
            return number_counter, start_num, num

        for position_x, line in enumerate(grid):
            start, number = 0, 0
            
            for position_y, element in enumerate(line):
                if element == '*':
                    gears.update({gears_counter: [position_x, position_y]})
                    gears_counter += 1
                
                if element == '.':
                    if number > 0:
                        counter, start, number = update_number(counter, number, position_x, start, position_y)

                if element.isdigit():
                    number = int(element) if number == 0 else number * 10 + int(element)
                    if start == 0:
                        start = position_y

                if not element.isdigit() and element != '.':
                    validators.update({validator_counter: [position_x, position_y]})
                    validator_counter += 1
                    if number > 0:
                        counter, start, number = update_number(counter, number, position_x, start, position_y)

                if len(line) == position_y + 1 and number > 0:
                    counter, start, number = update_number(counter, number, position_x, start, position_y)

        return grid_numbers, validators, gears
    
    @classmethod
    def level_1(cls, data):
        grid_numbers, validators, _ = cls.helper(data)
        validated = []

        def number_validator(grid):
            for _, position_in_grid in grid.items():
                number, line_x, start, end = position_in_grid[:]

                back_and_front = [value for value in range(start - 1 if start > 0 else start, end + 1 + 1)]

                for validator, validator_in_grid in list(validators.items()):
                    v_pos_x, v_pos_y = validator_in_grid[0], validator_in_grid[1]

                    if line_x == v_pos_x or line_x - 1 == v_pos_x or line_x + 1 == v_pos_x:
                        if v_pos_y in back_and_front:
                            validated.append(number)
                            break

                    if line_x - 1 > v_pos_x:
                        validators.pop(validator)

                    if v_pos_x - 1 > line_x:
                        break

            return validated

        return sum(number_validator(grid_numbers))
    
    

    @classmethod
    def level_2(cls, data):
        grid_numbers, _, gears = cls.helper(data)
        gear_ratio = []

        def add_numbers(_gear_y, _back_and_front, _temp_gear, _number):
            if _gear_y in _back_and_front:
                if _temp_gear == 0:
                    _temp_gear += _number
                    return _temp_gear
                
                if _temp_gear > 0:
                    _temp_gear *= _number
                    gear_ratio.append(_temp_gear)
                    _temp_gear = 0
                    return _temp_gear
            else:
                return _temp_gear   
        
        for position, gear in gears.items():
            gear_x, gear_y = gear[0], gear[1]
            temp_gear = 0

            for num_pos, position_in_grid in list(grid_numbers.items()):
                number, number_x, start, end = position_in_grid[:]
                back_and_front = [value for value in range(start - 1 if start > 0 else start, end + 1 + 1)]

                if gear_x - 1 == number_x:
                    temp_gear = add_numbers(gear_y, back_and_front, temp_gear, number)

                if gear_x == number_x:
                    temp_gear = add_numbers(gear_y, back_and_front, temp_gear, number)

                if gear_x + 1 == number_x:
                    temp_gear = add_numbers(gear_y, back_and_front, temp_gear, number)

        return sum(gear_ratio)


