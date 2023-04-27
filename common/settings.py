from pathlib import Path
import os


def get_path():
    path = Path(__file__)
    return path.parent.parent


def get_input_path(value):
    year = value
    root_dir = get_path()
    input_path = os.path.join(root_dir, 'input')

    for dirpath, dirnames, filenames in os.walk(input_path):
        dirnames.sort(reverse=True)
        latest_year = (dirnames[:1])[0]
        available_year = latest_year

        if year == available_year:
            return year
        if year != available_year:
            year = available_year
            return year


files = {
    'input_path': 'input/{year}/day{day}.txt',
    'file_path': 'input.{year}.day{day}.txt',
    'script_path': 'py.{year}.day{day}'
         }
