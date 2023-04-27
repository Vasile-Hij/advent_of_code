def daily_input(file_path, separator_two='\n\n'):
    return get_data_num(file_path, separator_two)


def get_data_num(file_path, separator_one=None, separator_two=None):
    with open(file_path, 'r') as file:
        return [[int(i) for i in x.split(separator_one)] for x in file.read().split(separator_two)]


def get_data_str(year, day):
    with open(f'input/{year}/day{day}.txt' 'r') as file:
        data = file.readlines()
        return list(map(str.strip, data))
