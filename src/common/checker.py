import logging
from datetime import date
from src.common.exceptions import ActionInFuture
from src.common.configs import BaseConfig
from termcolor import colored


logger = logging.getLogger(__name__)

INPUT_DAY_SHORT = 1
INPUT_DAY_LONG = 2
INPUT_YEAR_DAY = 4
FORMAT_YEAR = '%y'
FORMAT_MONTH = '%m'
FORMAT_DAY = '%d'


class InputCheck:
    @staticmethod
    def get_year():
        return str(date.today().strftime(FORMAT_YEAR))

    @staticmethod
    def get_month():
        return str(date.today().strftime(FORMAT_MONTH))

    @staticmethod
    def get_today():
        return str(date.today().strftime(FORMAT_DAY))
    
    current_year = get_year()
    month = get_month()
    today = get_today()
    
    @classmethod
    def check_year_day_input(cls, raw_value):
        value = str(raw_value)
        is_day = cls.input_day(value)
        is_year_day = cls.input_year_day(value)
        
        if is_day:
            year, day = is_day
            return year, day
    
        if is_year_day:
            year, day = is_year_day
            return year, day

    @classmethod
    def input_day(cls, value):
        day = value.strip()
        year = BaseConfig.get_input_path(cls.current_year)
        
        if cls.current_year == year and cls.month == 12 and cls.today < day:
            diff = day - cls.today
            msg_day = 'day' if len(diff) == 1 else 'days'
            raise ActionInFuture(f'You have to wait {diff} {msg_day}!')
            
        if day.isnumeric() and len(day) == INPUT_DAY_SHORT:
            day = f'0{day}'
            return year, day
    
        if day.isnumeric() and len(day) == INPUT_DAY_LONG:
            return year, day

    @classmethod
    def input_year_day(cls, value):
        clean_value = value.strip()
    
        if clean_value.isnumeric() and len(clean_value) == INPUT_YEAR_DAY:
            year = clean_value[:2]
            day = clean_value[2:]
            
            if year == cls.current_year and cls.month != '12':
                raise ActionInFuture('Wait until December and try to solve previous year!')
            
            if year > cls.get_year():
                raise ActionInFuture('That year is into the future! Try previous years!')
    
            if year < cls.current_year:
                print(colored("Let's go!", 'black', 'on_green', ['bold']))
             
            return year, day
