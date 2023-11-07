import logging
from datetime import date
from src.common.exceptions import Ignore
from src.common.configs import BaseConfig


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
    
    def clean_input(self, raw_value):
        value = str(raw_value)
        is_day = self.input_day(value)
        is_year_day = self.input_year_day(value)
        
        if is_day:
            year, day = is_day
            return year, day
    
        if is_year_day:
            year, day = is_year_day
            return year, day
        
    def input_day(self, value):
        day = value.strip()
        year = BaseConfig.get_input_path(self.current_year)
        
        if self.current_year == year and self.month == 12 and self.today < day:
            diff = day - self.today
            msg_day = 'day' if len(diff) == 1 else 'days'
            raise Ignore(f'You have to wait {diff} {msg_day}!')
            
        if day.isnumeric() and len(day) == INPUT_DAY_SHORT:
            day = f'0{day}'
            return year, day
    
        if day.isnumeric() and len(day) == INPUT_DAY_LONG:
            return year, day
        
    def input_year_day(self, value):
        clean_value = value.strip()
    
        if clean_value.isnumeric() and len(clean_value) == INPUT_YEAR_DAY:
            year = clean_value[:2]
            day = clean_value[2:]
            
            if year == self.current_year and self.month != '12':
                raise Ignore('Wait until December and try to solve previous year!')
            
            if year > self.get_year():
                raise Ignore('That year is into the future! Try previous years!')
    
            if year < self.current_year:
                print("Let's go!")
             
            return year, day
