import os
from pathlib import Path
from configparser import ConfigParser


def get_path():
    path = Path(__file__)
    return path.parent.parent


def get_input_path(value):
    year = value
    ROOT_DIR = get_path()
    input_path = os.path.join(ROOT_DIR, 'input')
    
    
    for dirpath, dirnames, filenames in os.walk(input_path):
        dirnames.sort(reverse=True)
        available_year = (dirnames[:1])[0]
        if year == available_year:
            return year
        if year != available_year:
            year = available_year
            return year


def get_config_file_auth():
    path = Path(__file__)
    ROOT_DIR = path.parent.parent.parent
    config_path = os.path.join(ROOT_DIR, '.config.cfg')
    config = ConfigParser()
    config.read(config_path)

    GITHUB_TOKEN = config.get('GitHub', 'token_gh')
    
    return GITHUB_TOKEN
