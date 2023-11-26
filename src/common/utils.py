import re
from typing import Tuple, List

separator = '─' * 100

    
class SolverFunctions:
    """
        File and text handler
    """
    
    @staticmethod
    def read_raw(source: str) -> str:
        with open(source, 'r') as file:
            return file.read()

    @staticmethod
    def write_file(source: str) -> str:
        with open(source, 'w') as file:
            return file.write(source)

    @staticmethod
    def make_tuple(method: callable, *sequences) -> Tuple:
        return tuple(map(method, *sequences))

    @staticmethod
    def make_list(method: callable, *sequences) -> List:
        return list(map(method, *sequences))
    
    """
        Strings operations
    """

    @classmethod
    def strings_per_line(cls, text) -> List[str]:
        text = cls.paragraph(text)
        return [[item for item in line.split('\n') if item] for line in text if line][0]

    @staticmethod
    def str_strip(text: str) -> str:
        return text.strip()

    @staticmethod
    def str_split(text: str) -> List[str]:
        return text.split()
    
    @staticmethod
    def check_len_string(text: str) -> bool:
        return True if len(text) > 1 else False
    
    @staticmethod
    def paragraph(text: str) -> str:
        return text.split('\n\n')

    @staticmethod
    def each_first_item(text: str) -> List[str]:
        return [item[0] for item in text]

    @staticmethod
    def each_item(data: str) -> List[str]:
        return [item for item in data]
    
    @classmethod
    def integers(cls, text: str) -> Tuple[int]:
        return cls.make_tuple(int, re.findall(r'-?[0-9]+', text))

    @classmethod
    def positive_integers(cls, text: str) -> Tuple[int]:
        return cls.make_tuple(int, re.findall(r'[0-9]+', text))

    @classmethod
    def find_digits(cls, text: str) -> Tuple[int]:
        return cls.make_tuple(int, re.findall(r'[0-9]', text))

    @classmethod
    def find_strings(cls, text: str) -> Tuple[str]:
        return cls.make_tuple(str, re.findall(r'[a-zA-Z]+', text))

    """
        Calculus
    """
    
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


Zero = (0, 0)
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