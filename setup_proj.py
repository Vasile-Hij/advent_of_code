import os
from configparser import MissingSectionHeaderError
from src.common.settings import get_config_value, make_setup
from src.common.exceptions import Ignore


paths_dir = {
    'cached_html': 'src/cached_html/{year}/',
    'input_path': 'src/input/{year}/',
    'input_path_day_sample': 'src/input/{year}/day{day}{sample}.txt',
    'input_path_day': 'src/input/{year}/day{day}.txt',
    'script_example': 'py/script_example.txt',   
    'created_script_path': 'py/{year}/day{day}.py',
    'script_path': 'py.{year}.day{day}',
    'year_path': 'py/{year}/',
    }

init = '__init__.py'

src_py = 'py/'
src_dir = 'src/'
src_common = 'src/common/'
src_input = 'src/input/'
src_cached_html = 'src/cached_html/'


def make_dir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    if not os.path.isfile(init):
        with open(f'{dir_name}{init}', 'w') as f:
            f.write('')
       
            
def get_setup():
    project, created = make_setup()
    if created:
        make_dir(src_py)
        make_dir(src_dir)
        make_dir(src_common) 
        make_dir(src_input) 
        make_dir(src_cached_html)
        
        raise Ignore('Everything is ok now! Run again!')
