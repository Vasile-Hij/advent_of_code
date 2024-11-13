import sys
import logging
from importlib import import_module
from collections import Counter
from typing import Tuple
from termcolor import colored

from src.common.exceptions import Ignore, ActionRequired
from src.common.setup_project import SetupProject
from src.aoc.aoc_client import AdventOfCodeBase
from src.common.configs import BaseConfig
from src.common.utils import SolverFunctions

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

lines = str.splitlines


class Display(SetupProject, BaseConfig, AdventOfCodeBase, SolverFunctions):
    @classmethod
    def helper_base(
            cls,
            source: str,
            year: str,
            title: str,
            handle_data: str,
            display: str,
            separator: int,
            parser_method: callable = str,
    ) -> Tuple:
        source_day_text, title, segmentation, method = source, title, handle_data, parser_method

        if parser_method:
            parser_method = cls.get_method(method)
        else:
            logger.warning(colored('Please add a "parser_method" in the day script!', 'black', 'on_red'))
            sys.exit()

        if segmentation != 'lines' or not segmentation:
            custom_segmentation = cls.get_method(segmentation)
            handle_data = custom_segmentation(source_day_text.rstrip())
        else:
            handle_data = lines(source_day_text.rstrip())

        print(colored(f'Year: 20{year} | {title}', 'black', 'on_light_grey', ['bold']))

        cls.display_items(title='Raw input', items=source_day_text.splitlines(), display=display, separator=separator)
        data = cls.make_tuple(parser_method, handle_data)
        cls.display_items(title='Parsed file', items=data, display=display, separator=separator)

        return data

    @classmethod
    def display_items(
            cls,
            *,
            title,
            items,
            display,
            separator
    ):
        if display:
            items_count = Counter(map(type, items))
            separate = '─' * separator

            def counter(all_items):
                """Count lines and verbose if plural"""
                for types, name in all_items.items():
                    return f'{name} {types.__name__}{"" if name == 1 else "s"}'

            print(f'{separate}\n{title}: {counter(items_count)}:\n{separate}')

            display = int(display)
            for line in items[0:display]:
                print(cls.truncate(line, width=separator))
            if display < len(items):
                print('...')

    @staticmethod
    def truncate(obj, width: int, dots: str = ' ...'):
        string = str(obj)
        if len(string) <= width:
            return string
        return string[: width - len(dots)] + dots

    @classmethod
    def get_results(
            cls,
            level: int,
            data: tuple,
            class_helper: list[callable, str],
            separator: int
    ):

        my_level = level
        script, class_name = class_helper
        class_name = getattr(script, class_name)

        match level:
            case 1:
                my_level = 'Level 1'

                cls._print_results(level=my_level, result=class_name.level_1(data), separator=separator)
                return class_name.level_1(data)

            case 2:
                my_level = 'Level 2'

                cls._print_results(level=my_level, result=class_name.level_2(data), separator=separator)
                return class_name.level_2(data)

    @staticmethod
    def _print_results(
            level: str,
            result: str,
            separator: int
    ):
        separate = '─' * separator
        print(
            f'{separate}\n',
            colored(f'{level}: {result}', 'light_green', 'on_black', ['bold']),
            f'\n{separate}'
        )

    @classmethod
    def check_required_files_exists(cls, year, day, level, sample):
        script_created = False
        input_data_created = False

        script_path = cls.paths_dir['script_path'].format(year=year, day=day)
        new_script_path = cls.paths_dir['new_script_path'].format(year=year, day=day)
        input_path_day = cls.paths_dir['input_path_day'].format(year=year, day=day)
        input_path_day_sample = cls.paths_dir['input_path_day_sample'].format(
            year=year,
            day=day,
            sample='_sample',
            level=level
        )
        input_path = cls.paths_dir['input_path'].format(year=year)
        year_path = cls.paths_dir['year_path'].format(year=year)

        try:
            script_module = import_module(script_path)
        except (ModuleNotFoundError, NameError):
            cls.make_dir(year_path)
            cls.write_file(new_script_path)
            logger.info(colored('Script created!', 'magenta', 'on_black'))

            text = cls.read_raw(cls.paths_dir['script_example'])
            added_blank_functions = list(text)

            with open(new_script_path, 'w') as file_text:
                file_text.writelines(added_blank_functions)
                logger.info(colored('New script was successfully populated!', 'magenta', 'on_black'))

            script_module = import_module(script_path)
            script_created = True

        try:
            input_data = cls.read_raw(input_path_day)
        except FileNotFoundError:
            available_year = cls.get_input_path(input_path)
            if available_year != year:
                cls.make_dir(input_path)
                logger.info(colored(f'Directory "src/input/{year}" have been created!', 'blue', 'on_black'))

            with open(input_path_day_sample, 'w') as f:
                f.write('')
            story_input = cls.get_story_input(year, day)

            with open(input_path_day, 'w') as f:
                for line in story_input:
                    f.write(line)

            input_data = cls.read_raw(input_path_day)
            input_data_created = True

        # if level == 2:
        #     cls.get_story_input(year, day)

        if sample:
            try:
                input_data = cls.read_raw(input_path_day_sample)
            except FileNotFoundError:
                with open(input_path_day_sample, 'w') as f:
                    f.write('')
                logger.warning(
                    colored(f'Sample file created without any data! '
                            f'Populate manually {input_path_day_sample} then run',
                            'light_yellow', 'on_black'))
                sys.exit()

        if script_created and input_data_created:
            logger.info(colored('Everything is setup. Just need to solve the quiz and run again!','black', 'on_light_yellow'))
            sys.exit()

        if sample and not input_data:
            logger.warning(
                colored('Samples need to be populated manually from AOC webpage!',
                        'light_yellow', 'on_black')
            )
            sys.exit()

        return script_module, input_data
