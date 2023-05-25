def start_day():
    name = '--- Day 6: Tuning Trouble ---'
    parser_function = 'str_strip'
    display_lines_or_paragraph = 'lines'
    return name, parser_function, display_lines_or_paragraph


def helper(data, stream_buffer):
    _data = data[0]
    for index, _ in enumerate(_data):
        if len(set(_data[index - stream_buffer : index])) == stream_buffer:
            return index


def part_1(data):
    message = helper(data, 4)
    return message


def part_2(data):
    message = helper(data, 14)
    return message
