def start_day():
    type_data = 'str'
    return type_data


def helper(data, stream_buffer):
    _data = data[0]
    for index, _ in enumerate(_data):
        if len(set(_data[index - stream_buffer: index])) == stream_buffer:
            return index


def part_1(data):
    message = helper(data, 4)
    return message


def part_2(data):
    message = helper(data, 14)
    return message
