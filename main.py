import argparse
import logging
from termcolor import colored

from src.common.checker import InputCheck
from src.common.exceptions import ActionRequired
from src.common.setup_project import SetupProject
from src.common.display import Display
from tests.tests import Test

logger = logging.getLogger(__name__)

TITLE = 'title'
PARSER_METHOD = 'parser_method'
HANDLE_DATA = 'handle_data'
SOLVER_CLASS = 'SolveTheDay'
DISPLAY = '10'
SEPARATOR = 150

if __name__ == '__main__':
    _help = """
            1.1 For year 2022 and day 01 type: "-v 2201".
            1.2 If you type only 2 digits and omit year, which it will be the latest year available in 'input' dir,
                it will run that day; days available from 01 to 25: "-l 01".
            2. Level 1 as each day contains 2 parts: 1 and 2. Commands is: "-l 1".
            3. For sample day test add "-s s".
            4. Sending results to "https://adventofcode.com/{year}/day/{day}/answer" add "-aoc true".

            Run input type <yearday> level 1: Run e.g.: python3 main.py -v 2201 -l 1
            Run input type <day> level 1 Run e.g.: python3 main.py -v 01 -l 1
            Run sample input for level 1: Run e.g.: python3 main.py -v 2201 -l 1 -s s
            Run input and submit: Run e.g.: python3 main.py -v 2201 -l 1 -aoc true 
           """

    class Command(InputCheck, Display):
        def cmd_arguments(self):
            parser = argparse.ArgumentParser(description="Run Advent of Code solution.")
            parser.add_argument('--value', '-v', type=int, help=_help)
            parser.add_argument('--level', '-l', type=int, help=_help)
            parser.add_argument('--sample', '-s', type=str, help=_help)
            parser.add_argument('--submit', '-aoc', type=bool, help=_help)
            args = parser.parse_args()

            year, day = self.check_year_day_input(args.value)
            level = args.level
            sample = args.sample
            submit_result = args.submit 

            return year, day, level, sample, submit_result

        def run(self):
            SetupProject.get_setup()
            Test.test_methods()
            
            year, day, level, sample, submit_result = self.cmd_arguments()
            
            if not level:
                raise ActionRequired(colored('Add which part you want to run e.g: "-l 1"', 'red', 'on_black'))
            
            script, input_data_exist = self.check_required_files_exists(year=year, day=day, level=level, sample=sample)

            title = getattr(script, TITLE)
            parser_method = getattr(script, PARSER_METHOD)
            handle_data = getattr(script, HANDLE_DATA)

            data = self.helper_base(
                source=input_data_exist, 
                year=year, 
                title=title,
                handle_data=handle_data,
                display=DISPLAY,
                separator=SEPARATOR,
                parser_method=parser_method,
            )
            
            result = self.get_results(
                level=level, 
                data=data,
                class_helper=[script, SOLVER_CLASS], 
                separator=SEPARATOR,
            )

            if submit_result and sample:
                raise ActionRequired(
                    colored('Results from sample cannot be send to AoC. Choose either testing a sample, '
                            'either sending the result. Recheck above helper info!', 'red', 'on_black'))
            
            if submit_result and not sample:
                level = {'a': '1', 'b': '2'}['a' if level == 1 else 'b']
                self.submit_answer(year=year, day=day, title=title, level=level, answer=result)

                
    runner = Command()
    runner.run()
    
    # CLASSES HELPER
    # class BaseConfig:
    # class InputCheck:
    # class SolverFunctions:
    
    # class Command(InputCheck, Display):

    # class Display(SetupProject, BaseConfig, AdventOfCodeBase, SolverFunctions):

    