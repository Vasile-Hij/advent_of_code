from datetime import date
from common.settings import get_input_path


INPUT_DAY_SHORT = 1
INPUT_DAY_LONG = 2
INPUT_YEAR_DAY = 4
FORMAT_YEAR = '%y'


def clean_input(raw_value):
    value = str(raw_value)
    current_year = int(get_time())
    year = get_input_path(current_year)

    is_day = input_day(value)
    is_year_day = input_year_day(value)

    if is_day:
        day = is_day
        return year, day

    if is_year_day:
        year, day = is_year_day
        return year, day


def input_day(value):
    clean_value = value.strip()
    if clean_value.isnumeric() and len(clean_value) == INPUT_DAY_SHORT:
        return f'0{value}'
    if clean_value.isnumeric() and len(clean_value) == INPUT_DAY_LONG:
        return value


def input_year_day(value):
    clean_value = value.strip()
    if clean_value.isnumeric() and len(clean_value) == INPUT_YEAR_DAY:
        year = clean_value[:2]
        day = clean_value[2:]
        return year, day


def get_time():
    return date.today().strftime(FORMAT_YEAR)
