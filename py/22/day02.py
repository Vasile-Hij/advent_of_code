"""
    Part_1:
        elf: A for Rock, B for Paper, and C for Scissors.
        you: X for Rock, Y for Paper, and Z for Scissors

        score calculation: 1 for Rock, 2 for Paper, and 3 for Scissors +
               outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)

    Part_2:
        second columns indicates now the output: X lose, Y draw, Z win, so find you had chosen
"""


def start_day():
    type_data = 'str'
    return type_data


def part_1(data):
    rules = {
        'A X': 1 + 3,
        'A Y': 2 + 6,
        'A Z': 3 + 0,
        'B X': 1 + 0,
        'B Y': 2 + 3,
        'B Z': 3 + 6,
        'C X': 1 + 6,
        'C Y': 2 + 0,
        'C Z': 3 + 3
    }

    return sum([rules[chance] for chance in data])


def part_2(data):
    new_rules = {
        'A X': 0 + 3,
        'A Y': 3 + 1,
        'A Z': 6 + 2,
        'B X': 0 + 1,
        'B Y': 3 + 2,
        'B Z': 6 + 3,
        'C X': 0 + 2,
        'C Y': 3 + 3,
        'C Z': 6 + 1
    }
    return sum([new_rules[chance] for chance in data])
