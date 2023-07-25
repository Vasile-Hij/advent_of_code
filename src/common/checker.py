from datetime import date

from src.common.exceptions import Ignore
from src.common.settings import get_input_path

INPUT_DAY_SHORT = 1
INPUT_DAY_LONG = 2
INPUT_YEAR_DAY = 4
FORMAT_YEAR = '%y'
FORMAT_MONTH = '%m'
FORMAT_DAY = '%d'


def get_year():
    return str(date.today().strftime(FORMAT_YEAR))


def get_month():
    return str(date.today().strftime(FORMAT_MONTH))


def get_today():
    return str(date.today().strftime(FORMAT_DAY))


current_year = get_year()
month = get_month()
today = get_today()


def clean_input(raw_value):
    value = str(raw_value)
    is_day = input_day(value)
    is_year_day = input_year_day(value)
    
    if is_day:
        year, day = is_day
        return year, day

    if is_year_day:
        year, day = is_year_day
        return year, day
    

def input_day(value):
    day = value.strip()
    year = get_input_path(current_year)
    
    if current_year == year and month == 12 and today < day:
        diff = day - today
        msg_day = 'day' if len(diff) == 1 else 'days'
        raise Ignore(f'You have to wait {diff} {msg_day}!')
        
    if day.isnumeric() and len(day) == INPUT_DAY_SHORT:
        day = f'0{day}'
        return year, day

    if day.isnumeric() and len(day) == INPUT_DAY_LONG:
        return year, day
    

def input_year_day(value):
    clean_value = value.strip()

    if clean_value.isnumeric() and len(clean_value) == INPUT_YEAR_DAY:
        year = clean_value[:2]
        day = clean_value[2:]
        
        if year == current_year and month != '12':
            raise Ignore(f'Wait until December and try to solve previous year!')
        
        if year > get_year():
            raise Ignore(f'That year is into the future! Try previous years!')

        if year < current_year:
            print("Let's go!")
        
        return year, day
