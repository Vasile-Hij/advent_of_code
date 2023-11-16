import argparse
import logging

from src.common.checker import InputCheck
from src.common.setup_project import SetupProject
from src.common.display import Display
from test.tests import Test

logger = logging.getLogger(__name__)

TITLE = 'title'
PARSER_METHOD = 'parser_method'
DISPLAY_TYPE = 'display_lines_or_paragraph'
SOLVER_CLASS = 'SolveTheDay'
PART_1 = 'part_1'
PART_2 = 'part_2'

if __name__ == '__main__':
    _help = """
            1. For year 2022 and day 01 type: -v 2201 ("-v" is value, "22" is directory , "01" is "day01") 
            2. If you type only 2 digits, it will be considered that day, but no more than 25 (if that day is solved yet),
            and year it will be the latest year available in 'input' directory.
            3. Sample day is taken by adding an "s" by the of digits: -v 01 -s s or -v 2201 -s s.
            4. Account states for signing to AOC using GitHub credentials: e.g: ... -a github

            Run e.g.: python3 main.py -v 01 -s s -a github'        
           """

    class Command(InputCheck, Display):
        def cmd_arguments(self):
            parser = argparse.ArgumentParser(description="Run Advent of Code solution.")
            parser.add_argument('--value', '-v', type=int, help=_help)
            parser.add_argument('--sample', '-s', type=str, help=_help)
            args = parser.parse_args()

            year, day = self.clean_input(args.value)
            sample = args.sample

            return year, day, sample

        def run(self):
            SetupProject.get_setup()
            Test.test_methods()
            
            year, day, sample = self.cmd_arguments()
            
            script, input_data_exist = self.check_required_files_exists(year=year, day=day, sample=sample)

            title = getattr(script, TITLE)
            parser_method = getattr(script, PARSER_METHOD)
            display_type = getattr(script, DISPLAY_TYPE)
            
            result = self.helper_base(
                source=input_data_exist, 
                year=year, 
                title=title,
                display_type=display_type,
                parser_method=parser_method
            )

            for each_day in [PART_1, PART_2]:
                self.printer(
                    each_day=each_day,
                    result=result,
                    class_helper=[script, SOLVER_CLASS]
                )

    runner = Command()
    runner.run()
    
    # CLASSES HELPER
    # class BaseConfig:
    # class InputCheck:
    # class SolverFunctions:
    
    # class Command(InputCheck, Display):

    # class Display(SetupProject, BaseConfig, AdventOfCodeBase, SolverFunctions):

    