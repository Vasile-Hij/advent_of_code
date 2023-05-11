from collections import deque
import re


def start_day():
    type_data = 'str_sep'
    sep = '\n\n'
    return type_data, sep


def helper(data):
    crates_data = data[0][:-1]
    operations_data = data[1]

    operation_number = 1
    operation = None
    operations = {operation_number: operation}
    crates = {}

    for letters_position in crates_data:
        for key, letter in enumerate(range(1, len(letters_position), 4)):
            key += 1
            if letters_position[letter] == " ":
                continue
            if key not in crates:
                crates[key] = deque(letters_position[letter])
            else:
                crates[key].appendleft(letters_position[letter])

    for operation in operations_data:
        operations[operation_number] = operation
        operation_number += 1

    return crates, operations


def part_1(data):
    crates, operations = helper(data)
    print(operations)
    arranged_crates = {}

    for operation in operations.values():
        # operation = operation.replace(' ', '').replace('move', '').replace('from', '').replace('to', '')
        # _move, _from, _to = operation.strip()
        _move, _from, _to = map(int, re.findall(r'\d+', operation))
    # todo

    return crates, operations


def part_2(data):
    return
