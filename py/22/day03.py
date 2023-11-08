def start_day():
    name = '--- Day 3: Rucksack Reorganization ---'
    parser_function = 'each_first_item'
    display_lines_or_paragraph = 'lines'
    return name, parser_function, display_lines_or_paragraph


def helper(data):
    return data


def part_1(data):
    counter = 0
    _data = helper(data)
    
    for char in _data:
        mid = len(char) // 2
        left = char[:mid]
        right = char[mid:]
    
        common, = set(left).intersection(right) 
        
        common = ord(common)
        char_a = ord('a') 
        char_A = ord('A')
        
        if common > char_a:
            counter += common - char_a + 1
        else:
            counter += common - char_A + 26 + 1
    
    return counter


def part_2(data):
    _data = helper(data)
    counter = 0
    
    for char in range(0, len(_data), 3):
        step = _data[char:char+3]

        common, = set(step[0]) & set(step[1]) & set(step[2]) 

        common = ord(common)
        char_a = ord('a') 
        char_A = ord('A')

        if common > char_a:
            counter += common - char_a + 1
        else:
            counter += common - char_A + 26 + 1

    return counter
