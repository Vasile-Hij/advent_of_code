import sys
import logging
from importlib import import_module
from collections import Counter
from typing import Tuple
from termcolor import colored

from src.common.setup_project import SetupProject
from src.aoc.aoc_client import AdventOfCodeBase
from src.common.configs import BaseConfig
from src.common.utils import SolverFunctions
from src.aoc.lxml_utils import HTMLHelper
from pathlib import Path

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

lines = str.splitlines


class Display(SetupProject, BaseConfig, AdventOfCodeBase, SolverFunctions):
    @classmethod
    def data_handler(
        cls,
        source: str,
        year: str,
        title: str,
        visual_handler_data: str,
        display_lines: int,
        width_separator: int,
        script: str,
        custom_parser_method: bool,
        parser_method: callable = str,
    ) -> Tuple:
        segmentation = visual_handler_data

        if segmentation != 'lines' or not segmentation:
            custom_segmentation = cls.get_method(segmentation)
            handled_data = custom_segmentation(source.rstrip())
        else:
            handled_data = lines(source.rstrip())

        if parser_method and not custom_parser_method:
            parser_method = cls.get_method(parser_method)
            data = cls.make_tuple(parser_method, handled_data)

        elif not parser_method and custom_parser_method:
            data = script.SolveTheDay.helper(source)

        else:
            logger.warning(
                colored(
                    'Please add a "parser_method" in the day script or change "custom_parser_method" to True',
                    'black',
                    'on_red',
                )
            )
            sys.exit()

        print(colored(f'Year: 20{year} | {title}', 'black', 'on_light_grey', ['bold']))
        cls.display_items(
            title='Raw input',
            items=source.splitlines(),
            display_lines=display_lines,
            width_separator=width_separator,
            custom_parser_method=False,
        )

        cls.display_items(
            title='Parsed input',
            items=data,
            display_lines=display_lines,
            width_separator=width_separator,
            custom_parser_method=custom_parser_method,
        )
        return data

    @classmethod
    def display_items(cls, title, items, display_lines, width_separator, custom_parser_method):
        if display_lines:
            if not items:
                logger.info(
                    colored('Your "helper" method does not return anything', 'red', 'on_black')
                )
                sys.exit()

            items_count = Counter(map(type, items))
            separate = '─' * width_separator

            def counter(all_items, items=items, custom=custom_parser_method):
                """Count lines and verbose if plural"""
                for types, name in all_items.items():
                    return f'{name} {types.__name__}{"" if name == 1 else "s"}{f" in {type(items).__name__}" if custom else ""}'

            print(f'{separate}\n{title}: {counter(items_count)}:\n{separate}')

            display_lines = int(display_lines)
            if custom_parser_method:

                if len(items) > display_lines:
                    parsed_long_list = list(items[0:display_lines])
                    parsed_long_list.append('...')
                    print(parsed_long_list)
                else:
                    print('Custom function may kill terminal to display parsed input!')
            else:
                for line in items[0:display_lines]:
                    print(cls.truncate(line, width_separator=width_separator))
                if display_lines < len(items):
                    print('...')

    @staticmethod
    def truncate(obj, width_separator: int, dots: str = ' ...'):
        string = str(obj)
        if len(string) <= width_separator:
            return string
        return string[: width_separator - len(dots)] + dots

    @classmethod
    def get_results(
        cls, level: int, data: any, class_helper: list[callable, str], width_separator: int
    ):

        script, class_name = class_helper
        class_name = getattr(script, class_name)

        match level:
            case 1:
                result = class_name.level_1(data)
                cls.display_results(level=level, result=result, width_separator=width_separator)
                return result

            case 2:
                result = class_name.level_2(data)
                cls.display_results(level=level, result=result, width_separator=width_separator)

                return result

    @staticmethod
    def display_results(level: str, result: str, width_separator: int):
        separate = '─' * width_separator
        print(
            f'{separate}\n',
            colored(f'{level}: {result}', 'light_green', 'on_black', ['bold']),
            f'\n{separate}',
        )

    @classmethod
    def check_required_files_exists(cls, year, day, level, sample):
        script_created = False
        input_data_created = False

        script_path = cls.paths_dir['script_path'].format(year=year, day=day)
        new_script_path = cls.paths_dir['new_script_path'].format(year=year, day=day)
        input_path_day = cls.paths_dir['input_path_day'].format(year=year, day=day)
        input_path_day_sample = cls.paths_dir['input_path_day_sample'].format(
            year=year, day=day, sample='_sample', level=level
        )
        input_path = cls.paths_dir['input_path'].format(year=year)
        year_path = cls.paths_dir['year_path'].format(year=year)

        try:
            input_data = cls.reader(input_path_day)
        except FileNotFoundError:
            available_year = cls.get_input_path(input_path)
            if available_year != year:
                cls.make_dir(input_path)
                logger.info(
                    colored(f'Directory "src/input/{year}" have been created!', 'blue', 'on_black')
                )

            story_input = cls.get_story_input(year, day)

            with Path.open(input_path_day, 'w') as f:
                last = len(story_input) - 1
                counter = 0

                for character in story_input:
                    if counter != last:
                        counter += 1
                        f.write(character)

            input_data = cls.reader(input_path_day)
            input_data_created = True
            logger.info(colored('Input was saved!', 'black', 'on_light_yellow'))

        try:
            script_module = import_module(script_path)
        except (ModuleNotFoundError, NameError):
            long_year, day = cls.get_long_year_and_day(year, day)
            cls.make_dir(year_path)

            title_of_the_day = cls.get_content(
                cls.urls['base_url'].format(year=long_year, day=day),
                selector='article[class="day-desc"] h2',
            )

            script_text = cls.reader(cls.paths_dir['script_example'])

            if 'day_to_change' in script_text:
                script_text  = script_text.replace('day_to_change', title_of_the_day)

            added_blank_functions = list(script_text)

            with Path.open(new_script_path, 'w') as file_text:
                file_text.writelines(added_blank_functions)
                logger.info(
                    colored('New script was successfully populated!', 'magenta', 'on_black')
                )

            script_module = import_module(script_path)
            script_created = True

        if sample:
            try:
                input_data = cls.reader(input_path_day_sample)
            except FileNotFoundError:
                cls.write_file(input_path_day_sample)
                logger.warning(
                    colored(
                        f'Sample file created without any data! '
                        f'Populate manually {input_path_day_sample} then run',
                        'light_yellow',
                        'on_black',
                    )
                )
                sys.exit()

        if script_created and input_data_created:
            logger.info(
                colored(
                    'Everything is setup. Just need to solve the quiz and run again!',
                    'black',
                    'on_light_yellow',
                )
            )
            sys.exit()

        if sample and not input_data:
            logger.warning(
                colored(
                    'Samples need to be populated manually from AOC webpage!',
                    'light_yellow',
                    'on_black',
                )
            )
            sys.exit()

        return script_module, input_data
