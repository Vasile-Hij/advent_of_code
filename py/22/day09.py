from typing import Set
from src.common.utils import SolverFunctions, Position_zero, Point, arrow_direction


title = 'Day'
parser_method = 'get_instructions'
display_lines_or_paragraph = 'paragraph'  # by default


class SolveTheDay(SolverFunctions):
    @staticmethod
    def helper(data):

        return data

    @classmethod
    def level_1(cls, data):
        def move_rope(motions, start=Position_zero) -> Set[Point]:
            head = tail = start
            visited = {start}
            for direction, step in motions[0]:
                for num in range(step):
                    head = cls.add_together(head, arrow_direction[direction])
                    tail = move_tail(tail, head)
                    visited.add(tail)
            return visited

        def move_tail(tail: Point, head: Point) -> Point:
            direction_x, direction_y = cls.sub(head, tail)
            if max(abs(direction_x), abs(direction_y)) > 1:
                tail = cls.add_together(tail, (cls.indication(direction_x), cls.indication(direction_y)))
            return tail

        return len(move_rope(data))

    @classmethod
    def level_2(cls, data):
        result = cls.helper(data)

        return