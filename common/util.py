import re
from importlib import import_module
from collections import Counter



separator = '─' * 100
lines = str.splitlines


def helper_base(source: str, year: str, functions: callable = str, display: int = 10) -> tuple:    
    day_text = read_raw(source)
    
    n, f, s = functions()
    name, function, segmentation = n.lower(), f.lower(), s.lower()
    parser_function = get_function(function)

    if segmentation != 'lines':
        custom_segmentation = get_function(segmentation)
        segmentation = custom_segmentation(day_text.rstrip())
    else:
        segmentation = lines(day_text.rstrip())


    _year = ''.join(['--- Year: 20', year])
    print(_year, name)

    display_items('Raw input', day_text.splitlines(), display)
    data = make_tuple(parser_function, segmentation)
    if parser_function != str or parser_function != lines:
        display_items('Parsed file', data, display)

    return data


def get_function(function: str):
    method_name = function
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(method_name)

    if not method:
        raise NotImplementedError(f'Method {method_name} not implemented')
    return method


def get_functions(*functions: str) -> list:
    return [get_function(func) for func in functions]


def display_items(file_raw, items, display: int, separate=separator):
    if display:
        type_input = Counter(map(type, items))

        def counter(types):
            """count lines and verbose if plural"""
            for types, name in types.items():
                return f'{name} {types.__name__}{"" if name == 1 else "s"}'

        print(f'{separate}\n{file_raw}: {counter(type_input)}:\n{separate}')
        for line in items[:display]:
            print(truncate(line))
        if display < len(items):
            print('...')


def check_required_files_exists(year, day, sample):
    input_path_sample = 'input/{year}/day{day}{sample}.txt'
    input_path = 'input/{year}/day{day}.txt'
    script_path = 'py.{year}.day{day}'
    created_script_path = 'py/{year}/day{day}.py'
    script_example = 'py/script_example.txt'
    

    
    try:
        script_exists = import_module(script_path.format(year=year, day=day))
    except (ModuleNotFoundError, NameError):
        write_file(created_script_path.format(year=year, day=day))
        print('Script created!')
        
        get_blank_text = read_raw(script_example)
        code_blank_to_day = [x for x in get_blank_text]
        
        script_created = created_script_path.format(year=year, day=day)

        with open(script_created, 'w') as file_text:
            file_text.writelines(code_blank_to_day)
        
        script_exists = import_module(script_path.format(year=year, day=day))
        
    
    if sample:
        try:
            input_path_exist = input_path_sample.format(year=year, day=day, sample="_sample")
        except FileNotFoundError:
            write_file(input_path_sample.format(year=year, day=day, sample=sample))
            print('Sample file created without data!')
            raise('populate file manually due mulptiple examples!')
    else:
        try:
            input_path_exist = input_path.format(year=year, day=day)
        except FileNotFoundError:
            print('making request')
            input_path_exist = write_file(input_path.format(year=year, day=day))
             
        
    return script_exists, input_path_exist


def read_raw(source: str) -> str:
    with open(source, 'r') as file:
        return file.read()
    
    
def write_file(source):
    with open(source, 'a') as file:
        return file.write(source)


def printer(part: str, result: str, func: callable = str, separate: str = separator):
    _part = part

    match part:
        case 'part_1':
            _part = 'Part 1'
        case 'part_2':
            _part = 'Part 2'

    results = f'{_part}: {func(result)}'
    print(f'{separate}\n{results}\n{separate}')


def truncate(obj, width: int = 100, ellipsis: str = ' ...'):
    string = str(obj)
    if len(string) <= width:
        return string
    return string[: width - len(ellipsis)] + ellipsis


def make_tuple(function: callable, *sequences) -> tuple:
    return tuple(map(function, *sequences))


def make_list(function: callable, *sequences) -> list:
    return list(map(function, *sequences))


def strings_per_line(data) -> list:
    _data = paragraph(data)
    return [[item for item in line.split('\n') if item] for line in _data if line][0]



def str_strip(data: str) -> str:
    return data.strip()


def str_split(data: str) -> str:
    return data.split()


def paragraph(data: str) -> str:
    return data.split('\n\n')


def integers(data: str) -> tuple[int]:
    return make_tuple(int, re.findall(r'-?[0-9]+', data))


def find_digits(text: str) -> tuple[int]:
    return make_tuple(int, re.findall(r'[0-9]', text))


def each_first_item(data: str) -> list[tuple]:
    return [item[0] for item in data]


def each_item(data: str) -> list[tuple]:
    return [item for item in data]


def find_strings(name):
    return tuple(re.findall(r'[a-zA-Z]', name))


def check_len_string(name) -> bool:
    return True if len(name) > 1 else False


four_directions = ((1, 0), (0, 1), (-1, 0), (0, -1))


def add_together(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sum_items(iterable, pred=bool) -> int:
    return sum(1 for item in iterable if pred(item))


class Matrix2D(dict):
    def __init__(self, grid=(), directions=four_directions, skip=(), default=KeyError):
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


def _product(numbers) -> float:
    result = 1
    for number in numbers:
        result *= number
    return result
