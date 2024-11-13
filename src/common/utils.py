import re
import operator
from typing import Tuple, List
from collections import abc

Position_zero = (0, 0)
Point = Tuple[int, ...]

four_directions = East, South, West, North = ((1, 0), (0, 1), (-1, 0), (0, -1))
diagonals = SE, NE, SW, NW = ((1, 1), (1, -1), (-1, 1), (-1, -1))
eight_directions = four_directions + diagonals
arrow_direction = {
    '.': Position_zero,
    'U': North, 'D': South, 'R': East, 'L': West
}


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
    def file_handler(source: str, json_data: str, mode: str = None):
        with open(source, f'{mode}') as file:
            file.write(json_data)

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
    def parse(text: Tuple) -> List[str]:
        return [elem for elem in text[0]]

    @staticmethod
    def check_len_string(text: str) -> bool:
        return True if len(text) > 1 else False

    @staticmethod
    def paragraph(text: str) -> List[str]:
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
    def find_digit(cls, text: str) -> Tuple[int]:
        return cls.make_tuple(int, re.findall(r'[0-9]', text))

    @classmethod
    def find_strings(cls, text: str) -> Tuple[str]:
        return cls.make_tuple(str, re.findall(r'[a-zA-Z]+', text))

    @classmethod
    def make_instructions(cls, text: str) -> List[Tuple[str, int]]:
        each_line = cls.strings_per_line(text)
        return [(instruction[:1], int(instruction[1:])) for instruction in each_line]

    @classmethod
    def split_two_in_list(cls, text: str) -> List[str]:
        each_line = cls.str_split(text)
        return [(line.split(':')[0]) for line in each_line]

    @classmethod
    def split_two_in_tuple(cls, text: str) -> Tuple[str, str]:
        each_line = cls.paragraph(text)

        for line in each_line:
            split = line.split()
            return split[0], split[1]

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
    def _product(numbers: list):
        result = 1
        for number in numbers:
            result *= number
        return result

    """
        Utils
    """

    @staticmethod
    def indication(x) -> int:  # "0, +1, or -1"
        return (0 if x == 0 else +1 if x > 0 else -1)

    @classmethod
    def range_generator(cls, number: int, start: int = 0, multiplier: int = 1):
        return [1 * multiplier for _ in range(start, number)]

    """
        Points in space
        p: numerator
        q: non-zero denominator
    """

    @classmethod
    def add(cls, p: Point, q: Point) -> Point:
        return cls.make_tuple(operator.add, p, q)

    @classmethod
    def sub(cls, p: Point, q: Point) -> Point:
        return cls.make_tuple(operator.sub, p, q)


class Matrix2D(dict):
    def __init__(self, grid=(), directions=four_directions, skip=(), default=KeyError):
        super().__init__()
        self.directions = directions
        self.default = default

        if isinstance(grid, abc.Mapping):
            self.update(grid)
        else:
            if isinstance(grid, str):
                grid = grid.splitlines()
            self.update(
                {
                    (x, y): value
                    for y, row in enumerate(grid)
                    for x, value in enumerate(row)
                    if value not in skip
                }
            )
