import argparse
from common.checker import clean_input
from common.settings import files
from common.util import daily_input
from importlib import import_module


def run(func, part, file_path):
    try:
        file_name = daily_input(file_path)
        print(f'{part}: {func(file_name)}')
    except FileNotFoundError:
        print("File not found!")


if __name__ == '__main__':
    _help = """
        1. For year 2022 and day 01 type: 2201 (meaning directory "22", "day01") 
        2. If you type only 2 digits, it will be considered that day, but no more than 25 (if that day is solved yet),
        and year it will be the latest year available in 'input' directory.
        3. Sample day is taken by adding an "s" by the of digits: 01s or 2201s.
    """

    parser = argparse.ArgumentParser(description="Run Advent of Code solution.")
    parser.add_argument('--year-day', '-i', type=int, help=_help)
    args = parser.parse_args()

    #year, day = clean_input(args)
    year, day = clean_input('01')

    file_path = files['file_path'].format(year=year, day=day)
    script_path = files['script_path'].format(year=year, day=day)
    input_path = files['input_path'].format(year=year, day=day)

    script = import_module(script_path)

    for part in ("part_1", "part_2"):
        if not hasattr(script, part):
            continue
        run(getattr(script, part), part, input_path)
