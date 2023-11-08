from collections import defaultdict
from pathlib import Path
from src.common.utils import SolverFunctions

title = 'Day 7: No Space Left On Device'
parser_method = 'str_split'
display_lines_or_paragraph = 'lines'


class SolveTheDay(SolverFunctions):
    @staticmethod
    def helper(_data):
        curr_dir = Path('/')
        dirs = defaultdict(int)

        for line in _data:
            match line:
                case ['$', 'cd', new_dir]:
                    curr_dir = curr_dir / new_dir
                    curr_dir = curr_dir.resolve()
                case [size, _] if size.isdigit():
                    size = int(size)
                    for path in [curr_dir, *curr_dir.parents]:
                        dirs[path] += size
        return dirs

    @classmethod
    def part_1(cls, data):
        maximum_size = 100000
        return sum(size for size in cls.helper(data).values() if size <= maximum_size)

    @classmethod
    def part_2(cls, data):
        available_space = 70000000
        required_space = 30000000
        dirs = cls.helper(data)
    
        return min(
            size for size in dirs.values() if dirs[Path('/')] - size <= available_space - required_space
        )
