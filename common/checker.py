from datetime import date
from settings import INPUT_PATH, get_path, get_input_path

INPUT_DAY = 2
INPUT_YEAR_DAY = 4
INPUT_DAY_SAMPLE = 3
INPUT_YEAR_DAY_SAMPLE = 5
SAMPLE = 's'
FORMAT_YEAR = '%y'


def clean_input(value):
    current_year = int(get_time())
    year = get_input_path(current_year)

    # import ipdb;
    # ipdb.set_trace(context=7)
    is_day = input_day(value)
    is_day_sample = input_day_sample(value)
    is_year_day = input_year_day(value)
    is_year_day_sample = input_year_day_sample(value)

    if is_day:
        day = int(is_day)
        return year, day

    if is_day_sample:
        day, sample = is_day_sample
        return year, day, sample

    if is_year_day:
        year, day = is_year_day
        return year, day

    if is_year_day_sample:
        year, day, sample = is_year_day_sample
        return year, day, sample


def input_day(value):
    clean_value = value.strip()
    if clean_value.isnumeric() and len(clean_value) == INPUT_DAY:
        return value


def input_day_sample(value):
    clean_value = value.strip()
    if clean_value.isnumeric() and len(clean_value) == INPUT_DAY_SAMPLE:
        day = clean_value[:2]
        sample = clean_value[-1]

        if sample != SAMPLE:
            print(f'Warning: Use "{SAMPLE}" from sample instead of {sample}')
        return day, sample


def input_year_day(value):
    clean_value = value.strip()
    if clean_value.isnumeric() and len(clean_value) == INPUT_YEAR_DAY:
        year = clean_value[:2]
        day = clean_value[2:]
        return year, day


def input_year_day_sample(value):
    clean_value = value.strip()
    if clean_value.isalnum() and len(clean_value) == INPUT_YEAR_DAY_SAMPLE:
        year = clean_value[:2]
        day = clean_value[2:3]
        sample = clean_value[-1]
        if sample != SAMPLE:
            print(f'Use "{SAMPLE}" from sample instead of {sample}')
        return year, day, sample


def get_time():
    return date.today().strftime(FORMAT_YEAR)


this_ = '22'
x = clean_input(this_)
print(x)

