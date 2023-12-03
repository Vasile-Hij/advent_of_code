from src.common.utils import SolverFunctions
import more_itertools 

title = 'Day'
parser_method = 'strings_per_line'
display_lines_or_paragraph = 'paragraph'  # by default


class SolveTheDay(SolverFunctions):    
    @classmethod
    def helper(cls, data):
        return data
    
    @classmethod
    def level_1(cls, data):
        result = cls.helper(data)
        total = 0

        for position, game in enumerate(result[0], start=1):
            sets_of_colors = game.split()[2:]
            cubes = {'red': 0, 'green': 0, 'blue': 0}
            increase = True
            
            for number, color in more_itertools.chunked(sets_of_colors, 2):
                color = color.replace(',', '').replace(';', '')
                cubes[color] = int(number)

                if cubes['red'] > 12 or cubes['green'] > 13 or cubes['blue'] > 14:
                    cubes.update({'red': 0, 'green': 0, 'blue': 0})
                    increase = False
                    break

            if increase:
                total += position

        return total
    
    @classmethod
    def level_2(cls, data):
        result = cls.helper(data)
        total = []

        for position, game in enumerate(result[0], start=1):
            sets_of_colors = game.split()[2:]
            cubes = {'red': 0, 'green': 0, 'blue': 0}

            for number, color in more_itertools.chunked(sets_of_colors, 2):
                color = color.replace(',', '').replace(';', '')
                number = int(number)
                
                color_value = cubes.get(color, None)
                if number > color_value:
                    cubes[color] = int(number)
            
            values = [value for value in cubes.values()]
            total.append(cls._product(values))
     
        return sum(total)
