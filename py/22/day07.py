from collections import defaultdict
from pathlib import Path


def start_day():
    type_data = 'str'
    return type_data


def helper(_data):
    curr_dir = Path('/')
    dirs = defaultdict(int)

    for line in _data:
        match line.split():
            case ['$', 'cd', new_dir]:
                curr_dir = curr_dir / new_dir
                curr_dir = curr_dir.resolve()
            case [size, _] if size.isdigit():
                size = int(size)
                for path in [curr_dir, *curr_dir.parents]:
                    dirs[path] += size
    return dirs


def part_1(data):
    maximum_size = 100000
    return sum(size for size in helper(data).values() if size <= maximum_size)


def part_2(data):
    available_space = 70000000
    required_space = 30000000
    dirs = helper(data)

    return min(size for size in dirs.values() if dirs[Path('/')] - size <= available_space - required_space)
