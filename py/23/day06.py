from src.common.utils import SolverFunctions

title = '--- Day 6: Wait For It ---'
parser_method = 'str_split'
display_lines_or_paragraph = 'lines'  # by default


class SolveTheDay(SolverFunctions):    
    @classmethod
    def helper(cls, time, distance):
        number = 1

        for race_time, race_distance in zip(time, distance):
            margin = 0
            for hold in range(race_time):
                if hold * (race_time - hold) > race_distance:
                    margin += 1

            number *= margin

        return number
    
    @classmethod
    def level_1(cls, data):
        time, distance = data
        time, distance = list(map(int, time[1:])), list(map(int, distance[1:]))

        return cls.helper(time, distance)

    @classmethod
    def level_2(cls, data):
        time, distance = data
        time, distance = [int(''.join(time[1:]))], [int(''.join(distance[1:]))]

        return cls.helper(time, distance)
