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
DISPLAY_TYPE = 'display_lines_or_paragraph'
SOLVER_CLASS = 'SolveTheDay'
DISPLAY = '10'

if __name__ == '__main__':
    _help = """
            1. For year 2022 and day 01 type: -v 2201 -l 1 ("-v" is value, "22" is directory , "01" is "day01" 
            while -l is level "1" as each day contains 2 parts) 
            2. If you type only 2 digits, it will be considered that day, but no more than 25 (if that day is solved yet),
            and year it will be the latest year available in 'input' directory.
            3. Sample day is taken by adding an "s" by the of digits: -v 01 -s s or -v 2201 -s s.
            4. Account states for signing to AOC using GitHub credentials: e.g: ... -a github

            Run sample input: Run e.g.: python3 main.py -v 2201 -l 1 -s s'
            Run input: Run e.g.: python3 main.py -v 2201 -l 1 -s s'
            Run input and submit: Run e.g.: python3 main.py -v 2201 -l 1 -aoc true'        
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
            
            script, input_data_exist = self.check_required_files_exists(year=year, day=day, level=level, sample=sample)

            title = getattr(script, TITLE)
            parser_method = getattr(script, PARSER_METHOD)
            display_type = getattr(script, DISPLAY_TYPE)
            
            data = self.helper_base(
                source=input_data_exist, 
                year=year, 
                title=title,
                display_type=display_type,
                display=DISPLAY,
                parser_method=parser_method
            )
            
            if not level:
                raise ActionRequired('Add which part you want to run e.g: "-l 1"')
            
            result = self.get_results(level=level, data=data, class_helper=[script, SOLVER_CLASS])

            if submit_result and sample:
                raise ActionRequired(
                    colored('Results from sample cannot be send to AoC. Choose either testing a sample, '
                            'either sending the result. Recheck above helper info!', 'red', 'on_black'))
            
            if submit_result and not sample:
                level = {'a': '1', 'b': '2'}['a' if level == 1 else 'b']
                submitted = self.submit_answer(year=year, day=day, level=level, answer=result)

                if submitted is True:
                    print(colored('Submitted were successful!', 'green', 'on_black'))
                else:
                    print(colored('Not submitted!', 'red', 'on_black'))
                
    runner = Command()
    runner.run()
    
    # CLASSES HELPER
    # class BaseConfig:
    # class InputCheck:
    # class SolverFunctions:
    
    # class Command(InputCheck, Display):

    # class Display(SetupProject, BaseConfig, AdventOfCodeBase, SolverFunctions):

    