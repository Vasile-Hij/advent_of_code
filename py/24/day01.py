from src.common.utils import SolverFunctions

title = 'Day'
parser_method = ''
custom_parser_method = True  # if True no parser method is required!!!
visual_handler_data = 'paragraph'  # by default


class SolveTheDay(SolverFunctions):
    @classmethod
    def helper(cls, data):
        data = data.split('\n')
        list_a, list_b = zip(*(s.split() for s in data))
        list_a = sorted([int(x) for x in list_a], reverse=True)
        list_b = sorted([int(x) for x in list_b], reverse=True)
        return list_a, list_b

    @classmethod
    def level_1(cls, data):
        result = 0

        for x, y in zip(data[0], data[1]):
            if x > y:
                result += x - y
            else:
                result += y - x
        return result

    @classmethod
    def level_2(cls, data):
        result = 0

        dict_y = {num: data[1].count(num) for num in set(data[1])}
        missing = set(data[0]).difference(data[1])

        for num in data[0]:
            if num in missing:
                continue
            result += dict_y[num] * num

        return result
