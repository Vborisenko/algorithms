from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers_set, double_losers_list = set(), set(), []
        winners.discard()
        for winner, loser in matches:
            winners.add(winner)
            if loser in losers_set:
                double_losers_list.append(loser)
            else:
                losers_set.add(loser)

        return [sorted(list(winners - set(losers_set))),sorted(list( losers_set - set(double_losers_list)))]


if __name__ == '__main__':
    print(Solution().findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
