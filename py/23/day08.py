from src.common.utils import SolverFunctions
from math import gcd

title = '--- Day 8: Haunted Wasteland ---'
parser_method = 'get_each_character'
visual_handler_data = 'paragraph'  # by default


class SolveTheDay(SolverFunctions):    
    @classmethod
    def helper(cls, data):
        commands, the_map = data
        commands = commands[0]
        mapped = {}
        
        for coord in the_map:
            key, values = coord.strip().split(' = ')
            left, right = values.replace('(', '').replace(')', '').replace(' ', '').split(',')
            mapped[key] = [left, right]

        return commands, mapped
    
    @classmethod
    def level_1(cls, data):
        commands, mapped = cls.helper(data)
        counter = 0
        actual = 'AAA'

        while actual != 'ZZZ':
            counter += 1
            actual = mapped[actual][0 if commands[0] == 'L' else 1]
            commands = commands[1:] + commands[0]
    
        return counter

    @classmethod
    def level_2(cls, data):
        commands, mapped = cls.helper(data)
        
        positions = [key for key in mapped if key.endswith('A')]
        visits = []
        
        for actual in positions:
            visit = []
            
            current_command = commands
            command_count = 0
            first_z = None
            
            while True:
                while command_count == 0 or not actual.endswith('Z'):
                    command_count += 1
                    actual = mapped[actual][0 if current_command[0] == 'L' else 1]
                    current_command = current_command[1:] + current_command[0]
                    
                visit.append(command_count)
                
                if first_z is None:
                    first_z = actual
                    command_count = 0
                elif actual == first_z:
                    break
                    
            visits.append(visit)
                    
        numbers = [visit[0] for visit in visits]
        least_common_number = numbers.pop()

        for number in numbers:
            least_common_number = least_common_number * number // gcd(least_common_number, number)
            
        return least_common_number
