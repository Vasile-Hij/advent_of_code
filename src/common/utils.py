import re

separator = '─' * 100

    
class SolverFunctions:   
    @staticmethod
    def read_raw(source: str) -> str:
        with open(source, 'r') as file:
            return file.read()

    @staticmethod
    def write_file(source):
        with open(source, 'w') as file:
            return file.write(source)

    @staticmethod
    def make_tuple(function: callable, *sequences) -> tuple:
        return tuple(map(function, *sequences))

    @staticmethod
    def make_list(function: callable, *sequences) -> list:
        return list(map(function, *sequences))
    
    def strings_per_line(self, data) -> list:
        data = self.paragraph(data)
        return [[item for item in line.split('\n') if item] for line in data if line][0]

    @staticmethod
    def str_strip(data: str) -> str:
        return data.strip()

    @staticmethod
    def str_split(data: str):
        return data.split()
    
    @staticmethod
    def paragraph(data: str):
        return data.split('\n\n')
    
    @classmethod
    def integers(cls, data: str) -> tuple[int]:
        return cls.make_tuple(int, re.findall(r'-?[0-9]+', data))
    
    def find_digits(self, text: str) -> tuple[int]:
        return self.make_tuple(int, re.findall(r'[0-9]', text))

    @staticmethod
    def each_first_item(self, data: str):
        return [item[0] for item in data]

    @staticmethod
    def each_item(data: str):
        return [item for item in data]

    @staticmethod
    def find_strings(name):
        return tuple(re.findall(r'[a-zA-Z]', name))
    
    @staticmethod
    def check_len_string(name) -> bool:
        return True if len(name) > 1 else False

    @staticmethod
    def add_together(a, b):
        return a[0] + b[0], a[1] + b[1]

    @staticmethod
    def sum_items(iterable, pred=bool) -> int:
        return sum(1 for item in iterable if pred(item))

    @staticmethod
    def _product(numbers) -> float:
        result = 1
        for number in numbers:
            result *= number
        return result


four_directions = ((1, 0), (0, 1), (-1, 0), (0, -1))


class Matrix2D(dict):
    def __init__(self, grid=(), directions=four_directions, skip=(), default=KeyError):
        super().__init__()
        self.directions = directions
        self.default = default

        self.update(
            {
                (x, y): value
                for y, row in enumerate(grid)
                for x, value in enumerate(row)
                if value not in skip
            }
        )