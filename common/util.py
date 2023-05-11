import re


def get_function(input_path, get_function_type, separator):
    def function_name(function):
        if function == 'int':
            return 'get_data_num'
        if function == 'str':
            return 'get_data_str'
        if function == 'str_sep':
            return 'get_data_str_sep'

    function_type = function_name(get_function_type)

    function_mapping = {
        'get_data_num': get_data_num,
        'get_data_str': get_data_str,
        'get_data_str_sep': get_data_str_sep
    }
    try:
        if separator is None:
            return function_mapping[function_type](input_path)
        return function_mapping[function_type](input_path, separator)
    except KeyError:
        print(f'This {function_type} is invalid!')


def unpack_values(start_day):
    separator = None
    try:
        function_type, separator = start_day()
    except ValueError:

        function_type = start_day()

    return function_type, separator


def get_data_num(input_path, separator=None):
    with open(input_path, 'r') as file:
        return [[int(item) for item in line.split() if item] for line in file.read().split(separator)]


def get_data_str(input_path):
    with open(input_path, 'r') as file:
        data = file.readlines()
        return list(map(str.strip, data))


def get_data_str_sep(input_path, separator=None):
    with open(input_path, 'r') as file:
        if separator:
            data = file.read().split(separator)
        else:
            data = file.read()
        return [[item for item in line.split('\n') if item] for line in data if line]
