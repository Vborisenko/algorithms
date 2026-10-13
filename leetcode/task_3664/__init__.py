from collections import defaultdict
from typing import List


class Solution:
    """ Idea of how to solve the task
        We can split cards into 3 columns:

        1st with cards type "x?"
        2nd with cards type "?x"
        3d  with cards type "xx"

        Let's calculate possible cards in 1st column.
        The main problem is in dublicate cards.

        aa aa aa aa aa ab ac ad
        8 = 5 + 3
        (8 - 2) // 2

        aa aa aa ab ac ad af ad ad

        if most frequence card as most_freq_x? > sum(x?) - most_freq_x,
        then our possible pairs is
    """
    @staticmethod
    def _get_max_freq_card(cards_counter) -> int:
        max_counter = 0
        for count in cards_counter.values():
            max_counter = max(max_counter, count)
        return max_counter

    def score(self, cards: List[str], x: str) -> int:
        cards_xy_counter = defaultdict(lambda: 0)
        cards_yx_counter = defaultdict(lambda: 0)
        sum_yx_cards = sum_xy_cards = 0
        cards_xx = 0

        for card in cards:
            if card[0] == card[1] == x:
                cards_xx += 1
            elif card[0] == x:
                cards_xy_counter[card] += 1
                sum_xy_cards += 1
            elif card[1] == x:
                cards_yx_counter[card] += 1
                sum_yx_cards += 1

        max_freq_counter_xy = self._get_max_freq_card(cards_xy_counter)
        max_freq_counter_yx = self._get_max_freq_card(cards_yx_counter)

        if cards_xx >= sum_xy_cards + sum_yx_cards:
            return sum_xy_cards + sum_yx_cards

        result = 0

        while cards_xx and  sum_xy_cards < 2 * max_freq_counter_xy:
            max_freq_counter_xy -= 1
            sum_xy_cards -= 1
            result += 1
            cards_xx -= 1

        while cards_xx and  sum_yx_cards < 2 * max_freq_counter_yx:
            max_freq_counter_yx -= 1
            sum_yx_cards -= 1
            result += 1
            cards_xx -= 1

        result += sum_xy_cards // 2
        result += sum_yx_cards // 2

        return result


if __name__ == "__main__":
    cards = ["ba","bc","bc","bb","bb","bb"]
    x = "b"
    Solution().score(cards, x)