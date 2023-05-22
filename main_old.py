import argparse
import logging
from common.checker import clean_input
from common.settings import files
from common.util_old import get_function, unpack_values
from importlib import import_module


def run(func, part, input_path, get_function_type, separator):
    try:
        result = get_function(input_path, get_function_type, separator)
        print(f'{part}: {func(result)}')
    except FileNotFoundError:
        logging.error("File not found!")


if __name__ == '__main__':
    _help = """
        1. For year 2022 and day 01 type: -v 2201 ("-v" is value, "22" is directory , "01" is "day01") 
        2. If you type only 2 digits, it will be considered that day, but no more than 25 (if that day is solved yet),
        and year it will be the latest year available in 'input' directory.
        3. Sample day is taken by adding an "s" by the of digits: -v 01 -s s or -v 2201 -s s.
    """

    parser = argparse.ArgumentParser(description="Run Advent of Code solution.")
    parser.add_argument('--value', '-v', type=int, help=_help)
    parser.add_argument('--sample', '-s', type=str, help=_help)
    args = parser.parse_args()

    year, day = clean_input(args.value)
    sample = args.sample

    script_path = files['script_path'].format(year=year, day=day)

    if sample:
        input_path = files['input_path'].format(year=year, day=day, sample="_sample")
    else:
        input_path = files['input_path'].format(year=year, day=day, sample='')

    script = import_module(script_path)
    print(f'year: {year}, day: {day}')

    for each_day in ("part_1", "part_2"):
        if not hasattr(script, 'start_day'):
            print('Please define input function and/or separator')
            continue

        start_day = getattr(script, 'start_day')
        get_function_type, separator = unpack_values(start_day)

        if not hasattr(script, each_day):
            continue
        run(getattr(script, each_day), each_day, input_path, get_function_type, separator)

