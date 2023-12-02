import json
import logging

from importlib import import_module
from collections import Counter
from typing import Tuple

from src.common.exceptions import Ignore, ActionRequired
from src.common.setup_project import SetupProject
from src.aoc.aoc_client import AdventOfCodeBase
from src.common.configs import BaseConfig
from src.common.utils import SolverFunctions
from termcolor import colored

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

lines = str.splitlines


class Display(SetupProject, BaseConfig, AdventOfCodeBase, SolverFunctions):
    separator = '─' * 100

    @classmethod
    def helper_base(
            cls,
            source: str, 
            year: str,
            title: str,
            display_type: str,
            display: str,
            parser_method: callable = str,
    ) -> Tuple:
        source_day_text, title, segmentation, method = source, title, display_type, parser_method,

        if parser_method:
            parser_method = cls.get_method(method)
        else:
            raise Ignore(colored('Please add a "parser_method" in the day script!', 'black', 'on_red'))

        if segmentation != 'lines' or not segmentation:
            custom_segmentation = cls.get_method(segmentation)
            segmentation = custom_segmentation(source_day_text.rstrip())
        else:
            segmentation = lines(source_day_text.rstrip())

        print(colored(f'--- Year: 20{year} | {title} ---', 'black', 'on_light_grey', ['bold']))

        cls.display_items(title='Raw input', items=source_day_text.splitlines(), display=display)
        data = cls.make_tuple(parser_method, segmentation)
        if parser_method != str or parser_method != lines:
            cls.display_items(title='Parsed file', items=data, display=display)

        return data

    @classmethod
    def display_items(
            cls,
            *,
            title, 
            items, 
            display, 
            separate=separator
    ):
        if display:
            items_count = Counter(map(type, items))
        
            def counter(all_items):
                """count lines and verbose if plural"""
                for types, name in all_items.items():
                    return f'{name} {types.__name__}{"" if name == 1 else "s"}'

            print(f'{separate}\n{title}: {counter(items_count)}:\n{separate}')
 
            display = int(display)
            for line in items[0:display]:
                print(cls.truncate(line))
            if display < len(items):
                print('...')

    @classmethod
    def get_results(
            cls,
            level: int,
            data: tuple,
            class_helper: list[callable, str],
    ):

        _level = level
        script, class_name = class_helper
        class_name = getattr(script, class_name)
        
        match level:
            case 1:
                _level = 'Level 1'
                cls._print_results(level=_level, result=class_name.level_1(data))
                return class_name.level_1(data)
            case 2:
                _level = 'Level 2'
                cls._print_results(level=_level, result=class_name.level_2(data))
                return class_name.level_2(data)

    @staticmethod
    def _print_results(
            level: str,
            result: str,
            separate: str = separator
    ):
        print(
            f'{separate}\n',
            colored(f'{level}: {result}', 'light_green', 'on_black', ['bold']),
            f'\n{separate}'
        )
     
    @staticmethod
    def truncate(obj, width: int = 100, dots: str = ' ...'):
        string = str(obj)
        if len(string) <= width:
            return string
        return string[: width - len(dots)] + dots
    
    @classmethod
    def check_required_files_exists(cls, year, day, level, sample):
        script_path = cls.paths_dir['script_path'].format(year=year, day=day)
        created_script_path = cls.paths_dir['created_script_path'].format(year=year, day=day)
        input_path_day = cls.paths_dir['input_path_day'].format(year=year, day=day)
        input_path_day_sample = cls.paths_dir['input_path_day_sample'].format(year=year, day=day, 
                                                                              sample='_sample', level=level)
        input_path = cls.paths_dir['input_path'].format(year=year)
        year_path = cls.paths_dir['year_path'].format(year=year)

        try:
            script_exists = import_module(script_path)
        except (ModuleNotFoundError, NameError):
            cls.make_dir(year_path)
            cls.write_file(created_script_path)
            logger.info(colored(f'Script created!', 'magenta', 'on_black'))

            _text = cls.read_raw(cls.paths_dir['script_example'])
            added_blank_functions = [x for x in _text]

            with open(created_script_path, 'w') as file_text:
                file_text.writelines(added_blank_functions)
                logger.info(colored('New script successfully populated!', 'magenta', 'on_black'))

            script_exists = import_module(script_path)

        try:
            input_data = cls.read_raw(input_path_day)
        except FileNotFoundError:
            available_year = cls.get_input_path(input_path)
            if available_year != year:
                cls.make_dir(input_path)
                logger.info(colored(f'Directory "src/input/{year}" have been created!', 'blue', 'on_black'))

            with open(input_path_day_sample, 'w') as f:
                f.write('')
            aoc_input = cls.get_aoc_data(year, day, level)

            with open(input_path_day, 'w') as f:
                for line in aoc_input:
                    f.write(line)

            input_data = cls.read_raw(input_path_day)
            
        if level == 2:
            cls.get_aoc_data(year, day, level,)
                
        if sample:
            try:
                input_data = cls.read_raw(input_path_day_sample)
            except FileNotFoundError:
                with open(input_path_day_sample, 'w') as f:
                    f.write('')
                raise ActionRequired(
                    colored('Sample file created without data! Populate and rerun!', 'light_yellow', 'on_black'))

        if sample and not input_data:
            raise ActionRequired(
                colored('Samples need to be populated manually from AOC webpage!', 
                        'light_yellow', 'on_black')
            )
            
        return script_exists, input_data
