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
    name = '--- Day 2: Rock Paper Scissors ---'
    parser_function = 'str_split'
    display_lines_or_paragraph = 'lines'
    return name, parser_function, display_lines_or_paragraph


def helper(data):
    return data


def part_1(data):
    answer = 0

    for line in data:
        left, right = line
        left = "ABC".index(left)
        right = "XYZ".index(right)

        answer += right + 1

        match (right - left) % 3:
            case 1:
                answer += 6
            case 0:
                answer += 3

    return answer


def part_2(data):
    answer = 0

    for line in data:
        left, right = line
        left = "ABC".index(left)

        match right:
            case "X":
                answer += (left - 1) % 3 + 1
            case "Y":
                answer += 3
                answer += left + 1
            case "Z":
                answer += 6
                answer += (left + 1) % 3 + 1

    return answer
