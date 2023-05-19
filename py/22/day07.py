from collections import deque

def start_day():
    type_data = 'str'
    return type_data


def helper(data):
    current_dir_letter = 'root'  # directory as default
    dir_letter = []  # a, d, e
    temp_dir_letter = []  # a, e -> a -> d
    dirs = {}

    _data = data

    if data[0] == '$ cd /':
        _data = data[1:]

    for index, value in enumerate(_data):
        try:
            first, second, current_dir_letter = value.split()[0], value.split()[1], value.split()[2]
        except IndexError:
            first, second = value.split()[0], value.split()[1]

        if first == '$' and second == 'ls':
            continue

        if first == 'dir' and second.isalpha():
            dir_letter.append(second)
            continue

        if first == '$' and second == 'cd' and current_dir_letter.isalpha():
            temp_dir_letter.append(current_dir_letter)
            continue

        if first.isnumeric() and current_dir_letter in temp_dir_letter:
            if len(temp_dir_letter) > 1:
                first_letter = temp_dir_letter[:1][0]
                dirs.setdefault(first_letter, []).append(first)
            else:
                dirs.setdefault(current_dir_letter, []).append(first)
            continue

        if first == '$' and second == 'cd' and current_dir_letter == '..':
            temp_dir_letter.remove(str(temp_dir_letter[-1]))
            continue

    for letter, size in dirs.items():
        total_size = sum(int(item) for item in size)
        dirs[letter] = total_size

    return dirs


def part_1(data):
    maximum_size = 100000
    dirs = helper(data)

    return sum(x for x in dirs.values() if x <= maximum_size)



def part_2(data):
    message = helper(data)
    return message