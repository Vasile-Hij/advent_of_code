def get_input_num(day, separator_one=None, separator_two=None):
    with open(f'./input/{day}.txt', 'r') as file:
        return [[int(i) for i in x.split(separator_one)] for x in file.read().split(separator_two)]