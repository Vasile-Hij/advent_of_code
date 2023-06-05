import argparse
import sys
from common.checker import clean_input #check_maximum_availability
from common.settings import files, get_credentials
from common.util import helper_base, printer, check_required_files_exists
from importlib import import_module


if __name__ == '__main__':
    _help = """
            1. For year 2022 and day 01 type: -v 2201 ("-v" is value, "22" is directory , "01" is "day01") 
            2. If you type only 2 digits, it will be considered that day, but no more than 25 (if that day is solved yet),
            and year it will be the latest year available in 'input' directory.
            3. Sample day is taken by adding an "s" by the of digits: -v 01 -s s or -v 2201 -s s.
            4. Account states for signing to AOC using GitHub cedentials: e.g: ... -a github
            
            Run e.g.: python3 main.py -v 01 -s s -a github'        
           """

    parser = argparse.ArgumentParser(description="Run Advent of Code solution.")
    parser.add_argument('--value', '-v', type=int, help=_help)
    parser.add_argument('--sample', '-s', type=str, help=_help)
    parser.add_argument('--account_name', '-a', type=str, help=_help)
    args = parser.parse_args()

    year, day = clean_input(args.value)
    sample = args.sample
    account_name = args.account_name
    
    # if account_name:
    #     username, password = get_credentials(account_name)
    #     print(username, password )

    script, input_path = check_required_files_exists(year=year, day=day, sample=sample)

  
    if not all(hasattr(script, checker) for checker in ['start_day', 'helper', 'part_1', 'part_2']):
        print(f'Please define all functions as in "blank.txt" template')
            
    functions = getattr(script, 'start_day')
    result = helper_base(source=input_path, year=year, functions=functions)

    for each_day in ["part_1", "part_2"]:
        printer(part=each_day, result=result, func=getattr(script, each_day))
