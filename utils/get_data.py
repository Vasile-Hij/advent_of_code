def get_data_num(year, day, separator_one=None, separator_two=None):
    with open(f'./raw_data/{year}/{day}', 'r') as file:
        return [[int(i) for i in x.split(separator_one)] for x in file.read().split(separator_two)]


def get_data_str(year, day):
    with open(f'./raw_data/{year}/{day}', 'r') as file:
        data = file.readlines()
        return list(map(str.strip, data))