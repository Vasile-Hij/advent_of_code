from datetime import date
from settings import get_input_path


INPUT_DAY = 2
INPUT_YEAR_DAY = 4
INPUT_DAY_SAMPLE = 3
INPUT_YEAR_DAY_SAMPLE = 5
SAMPLE_LETTER = 's'
SAMPLE_DAY = {'sample_day': "{day}_sample"}
FORMAT_YEAR = '%y'


def clean_input(value):
    current_year = int(get_time())
    year = get_input_path(current_year)

    is_day = input_day(value)
    is_day_sample = input_day_sample(value)
    is_year_day = input_year_day(value)
    is_year_day_sample = input_year_day_sample(value)

    if is_day:
        day = is_day
        return year, day

    if is_day_sample:
        day = is_day_sample
        return year, day

    if is_year_day:
        year, day = is_year_day
        return year, day

    if is_year_day_sample:
        year, day = is_year_day_sample
        return year, day


def input_day(value):
    clean_value = value.strip()
    if clean_value.isnumeric() and len(clean_value) == INPUT_DAY:
        return value


def input_day_sample(value):
    clean_value = value.strip()
    if clean_value.isalnum() and len(clean_value) == INPUT_DAY_SAMPLE:
        day = clean_value[:2]
        sample = clean_value[-1]

        if sample != SAMPLE_LETTER:
            print(f'Warning: Use "{SAMPLE_LETTER}" from sample instead of "{sample}".')
        sample_day = SAMPLE_DAY['sample_day'].format(day=day)
        return sample_day


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
        day = clean_value[2:4]
        sample = clean_value[-1]
        if sample != SAMPLE_LETTER:
            print(f'Use "{SAMPLE_LETTER}" from "sample" instead of "{sample}".')
        sample_day = SAMPLE_DAY['sample_day'].format(day=day)
        return year, sample_day


def get_time():
    return date.today().strftime(FORMAT_YEAR)
