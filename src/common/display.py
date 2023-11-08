import sys
import logging

from importlib import import_module
from collections import Counter

from src.common.exceptions import Ignore
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
            parser_method: callable = str,
            display: str = 10
    ) -> tuple:
        source_day_text, title, segmentation, method = source, title, display_type.lower(), parser_method.lower(),
        
        if parser_method:
            parser_method = cls.get_method(method)
        else:
            raise Ignore(colored('Please add a "parser_method" in the day script!', 'black', 'on_red'))

        if segmentation != 'lines' or segmentation is None:
            custom_segmentation = cls.get_method(segmentation)
            segmentation = custom_segmentation(source_day_text.rstrip())
        else:
            segmentation = lines(source_day_text.rstrip())

        print(colored(f'--- Year: 20{year} | {title} ---', 'black', 'on_light_grey', ['bold']))

        cls.display_items(cls, 'Raw input', source_day_text.splitlines(), display)
        data = cls.make_tuple(parser_method, segmentation)
        if parser_method != str or parser_method != lines:
            cls.display_items(cls, 'Parsed file', data, display)

        return data

    def display_items(
            self, 
            title, 
            items, 
            display, 
            separate=separator
    ):
        if display:
            items_count = Counter(map(type, items))
        
            def counter(items_count):
                """count lines and verbose if plural"""
                for types, name in items_count.items():
                    return f'{name} {types.__name__}{"" if name == 1 else "s"}'

            print(f'{separate}\n{title}: {counter(items_count)}:\n{separate}')
            for line in items[:display]:
                print(self.truncate(line))
            if display < len(items):
                print('...')

    @classmethod
    def printer(
            cls,
            each_day: str,
            result: tuple,
            class_helper: list[callable, str],
            separate: str = separator
    ):
        _part = each_day
        script, class_name = class_helper
        class_name = getattr(script, class_name)
        
        match each_day:
            case 'part_1':
                _part = 'Part 1'
                results = f'{_part}: {class_name.part_1(result)}'
            case 'part_2':
                _part = 'Part 2'
                results = f'{_part}: {class_name.part_2(result)}'
        
        print(
            f'{separate}\n',
            colored(f'{results}', 'light_green', 'on_black', ['bold']),
            f'\n{separate}'
        )
     
    @staticmethod
    def truncate(obj, width: int = 100, dots: str = ' ...'):
        string = str(obj)
        if len(string) <= width:
            return string
        return string[: width - len(dots)] + dots

    def check_required_files_exists(self, year, day, sample):
        script_path = self.paths_dir['script_path'].format(year=year, day=day)
        created_script_path = self.paths_dir['created_script_path'].format(year=year, day=day)
        input_path_day = self.paths_dir['input_path_day'].format(year=year, day=day)
        input_path_day_sample = self.paths_dir['input_path_day_sample'].format(year=year, day=day, sample='_sample')
        input_path = self.paths_dir['input_path'].format(year=year)
        year_path = self.paths_dir['year_path'].format(year=year)

        try:
            script_exists = import_module(script_path)
        except (ModuleNotFoundError, NameError):
            self.make_dir(year_path)
            self.write_file(created_script_path)
            logger.info(f'Script created!')

            _text = self.read_raw(self.paths_dir['script_example'])
            added_blank_functions = [x for x in _text]

            with open(created_script_path, 'w') as file_text:
                file_text.writelines(added_blank_functions)
                logger.info('New script successfully populated!')

            script_exists = import_module(script_path)

        try:
            input_data_exist = self.read_raw(input_path_day)
        except FileNotFoundError:
            available_year = self.get_input_path(input_path)
            if available_year != year:
                self.make_dir(input_path)
                logger.info(f'Directory "src/input/{year}" have been created!')

            with open(input_path_day_sample, 'w') as f:
                f.write('')
            aoc_input = self.get_aoc_data(year, day)

            with open(input_path_day, 'w') as f:
                for line in aoc_input:
                    f.write(line)

            input_data_exist = self.read_raw(input_path_day)

        if sample:
            try:
                input_data_exist = self.read_raw(input_path_day_sample)
            except FileNotFoundError:
                with open(input_path_day_sample, 'w') as f:
                    f.write('')
                logger.info('Sample file created without data!')
                logger.info('Populate file manually due multiple examples!')  # TO DO: find a pattern to automate it

        return script_exists, input_data_exist
