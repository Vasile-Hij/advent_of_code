def start_day():
    type_data = 'str'
    return type_data


def part_1(data):
    counter = 0
    
    for char in data:
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
    counter = 0
    
    for char in range(0, len(data), 3):
        step = data[char:char+3]

        common, = set(step[0]) & set(step[1]) & set(step[2]) 

        common = ord(common)
        char_a = ord('a') 
        char_A = ord('A')

        if common > char_a:
            counter += common - char_a + 1
        else:
            counter += common - char_A + 26 + 1

    return counter
