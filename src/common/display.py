import sys
import logging

from importlib import import_module
from collections import Counter

from src.common.setup_project import SetupProject
from src.aoc.aoc_client import AdventOfCodeBase
from src.common.configs import BaseConfig
from src.common.utils import separator, SolverFunctions


logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Display(SetupProject, BaseConfig, AdventOfCodeBase, SolverFunctions):
    lines = str.splitlines

    @classmethod
    def helper_base(cls, source: str, year: str, methods: callable = str, display: int = 10) -> tuple:
        day_text = source
        name, method, display_type = methods()
        name, method, segmentation = name.lower(), method.lower(), display_type.lower()

        parser_function = cls.get_method(method)

        if segmentation != 'lines' or segmentation is None:
            custom_segmentation = cls.get_method(segmentation)
            segmentation = custom_segmentation(day_text.rstrip())
        else:
            segmentation = cls.lines(day_text.rstrip())

        _year = f'--- Year: 20{year}'
        print(_year, name)

        cls.display_items(cls, 'Raw input', day_text.splitlines(), display)
        data = cls.make_tuple(parser_function, segmentation)
        if parser_function != str or parser_function != cls.lines:
            cls.display_items('Parsed file', data, display)

        return data

    def display_items(self, file_raw, items, display: int, separate=separator):
        if display:
            type_input = Counter(map(type, items))

            def counter(types):
                """count lines and verbose if plural"""
                for types, name in types.items():
                    return f'{name} {types.__name__}{"" if name == 1 else "s"}'

            print(f'{separate}\n{file_raw}: {counter(type_input)}:\n{separate}')
            for line in items[:display]:
                print(self.truncate(line))
            if display < len(items):
                print('...')

    @staticmethod
    def printer(part: str, result: str, func: callable = str, separate: str = separator) -> tuple:
        _part = part

        match part:
            case 'part_1':
                _part = 'Part 1'
            case 'part_2':
                _part = 'Part 2'

        results = f'{_part}: {func(result)}'
        print(f'{separate}\n{results}\n{separate}')

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
