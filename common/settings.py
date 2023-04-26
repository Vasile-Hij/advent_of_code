from configparser import ConfigParser
from pathlib import Path
import os


def get_path():
    path = Path(__file__)
    return path.parent.parent


def get_setting(file, variable):
    root_dir = get_path()
    config_path = os.path.join(root_dir, 'settings.ini')
    config = ConfigParser()
    config.read(config_path)
    return config.get(file, variable)


def get_input_path(value):
    year = value
    root_dir = get_path()
    input_path = os.path.join(root_dir, INPUT_PATH)

    for dirpath, dirnames, filenames in os.walk(input_path):
        dirnames.sort(reverse=True)
        latest_year = (dirnames[:1])[0]
        available_year = int(latest_year)

        if year == available_year:
            return year
        if year != available_year:
            year = available_year
            return year


INPUT_PATH = get_setting('SETTINGS', 'INPUT_PATH')
SCRIPT_PATH = get_setting('SETTINGS', 'SCRIPT_PATH')
COMMON_PATH = get_setting('SETTINGS', 'COMMON_PATH')

