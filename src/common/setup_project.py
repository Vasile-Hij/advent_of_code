import logging
import os

from termcolor import colored

from src.common.configs import BaseConfig

logger = logging.getLogger(__name__)


class SetupProject:
    paths_dir = {
        'input_path': 'src/input/{year}/',
        'input_path_day_sample': 'src/input/{year}/day{day}{sample}_{level}.txt',
        'input_path_day': 'src/input/{year}/day{day}.txt',
        'script_example': 'py/script_example.txt',   
        'new_script_path': 'py/{year}/day{day}.py',
        'script_path': 'py.{year}.day{day}',
        'year_path': 'py/{year}/',
        'results_file': 'src/results/result.json'
        }
    
    init_file = '__init__.py'
    src_py = '../../py/'
    src_dir = '../'
    src_common = '/'
    src_input = '../input/'
    src_results = '../results/'
    
    @classmethod
    def make_dir(cls, dir_name):
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        if not os.path.isfile(cls.init_file):
            with open(f'{dir_name}{cls.init_file}', 'w') as f:
                f.write('')

    @classmethod
    def get_setup(cls):
        project, created = BaseConfig.make_setup()
        if created:
            cls.make_dir(cls.src_py)
            cls.make_dir(cls.src_dir)
            cls.make_dir(cls.src_common) 
            cls.make_dir(cls.src_input) 
            cls.make_dir(cls.src_results)
            
            logger.info(colored('Everything is ok now! Run again!', 'green', 'on_black'))
