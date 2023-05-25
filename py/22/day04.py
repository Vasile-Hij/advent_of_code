def start_day():
    name = '--- Day 4: Camp Cleanup ---'
    parser_function = 'str_strip'
    display_lines_or_paragraph = 'lines'
    return name, parser_function, display_lines_or_paragraph


find_range = lambda first, second: range(first, second + 1)


def helper(data):
    return 


def part_1(data):
    counter = 0
    for each_pair in data:
        first, second = each_pair.strip().split(',')
        first = set(find_range(*map(int, first.split('-'))))
        second = set(find_range(*map(int, second.split('-'))))
        # if len(first - second) == 0 or len(second - first) == 0:
        if first.issubset(second) or second.issubset(first):
            counter += 1
    return counter


def part_2(data):
    counter = 0
    for each_pair in data:
        first, second = each_pair.strip().split(',')
        first = set(find_range(*map(int, first.split('-'))))
        second = set(find_range(*map(int, second.split('-'))))
        if len(first & second) > 0:
            counter += 1

    return counter
