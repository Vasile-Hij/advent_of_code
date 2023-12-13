from collections import Counter
from functools import cmp_to_key

from src.common.utils import SolverFunctions

title = '--- Day 7: Camel Cards ---'
parser_method = 'split_two_in_tuple'
handle_data = 'lines'  # by default


class SolveTheDay(SolverFunctions):
    @classmethod
    def helper(cls, data, rank, card_rank):
        def compare_to_key(h1, h2):
            h1 = h1[0]
            h2 = h2[0]

            hand_1 = rank(h1)
            hand_2 = rank(h2)
            if hand_1 != hand_2:
                if hand_1 > hand_2:
                    return 1
                else:
                    return -1
            else:
                for elem in range(5):
                    if card_rank[h1[elem]] > card_rank[h2[elem]]:
                        return 1
                    if card_rank[h1[elem]] < card_rank[h2[elem]]:
                        return -1
            return 0

        return compare_to_key, sum([rank * int(bid) for rank, (hand, bid) in enumerate(data, 1)])

    @classmethod
    def level_1(cls, data):
        data = list(data)
        card_rank = {
            'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2
        }

        def rank(hand):
            counter = Counter(hand)
            most_common = counter.most_common()
            if most_common[0][1] == 5:
                return 7
            if most_common[0][1] == 4:
                return 6
            if most_common[0][1] == 3 and most_common[1][1] == 2:
                return 5
            if most_common[0][1] == 3:
                return 4
            if most_common[0][1] == 2 and most_common[1][1] == 2:
                return 3
            if most_common[0][1] == 2:
                return 2
            return 1

        compare_to_key, _ = cls.helper(data, rank, card_rank)
        
        data.sort(key=cmp_to_key(compare_to_key))
        _, total = cls.helper(data, rank, card_rank)
        return total

    @classmethod
    def level_2(cls, data):
        data = list(data)
        card_rank = {
            'A': 12, 'K': 11, 'Q': 10, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1, 'J': 0
        }

        def new_rank(hand):
            counter = Counter(hand)
            counter_j = counter['J']
            del counter['J']

            most_common = counter.most_common()

            if len(most_common) <= 1:
                return 7
            if most_common[0][1]+counter_j == 5:
                return 7
            if most_common[0][1]+counter_j == 4:
                return 6
            if (most_common[0][1]+counter_j == 3 and most_common[1][1] == 2) or \
                    (most_common[0][1] == 3 and most_common[1][1]+counter_j == 2):
                return 5
            if most_common[0][1]+counter_j == 3:
                return 4
            if (most_common[0][1]+counter_j == 2 and most_common[1][1] == 2) or \
                    (most_common[0][1] == 2 and most_common[1][1]+counter_j == 2):
                return 3
            if most_common[0][1]+counter_j == 2:
                return 2
            return 1

        compare_to_key, _ = cls.helper(data, new_rank, card_rank)

        data.sort(key=cmp_to_key(compare_to_key))
        _, total = cls.helper(data, new_rank, card_rank)
        return total
    