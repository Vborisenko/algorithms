import heapq
from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        sorted_collections = sorted(list(zip(startTime, endTime, profit)), key=lambda x: x[0])

        def dp() -> list:
            st_time, end_time, value = 0, 1, 2
            d = [_[value] for _ in sorted_collections]

            for i in range(len(sorted_collections)):
                for j in range(i):
                    if sorted_collections[i][st_time] >= sorted_collections[j][end_time]:
                        d[i] = max(d[i], d[j] + sorted_collections[i][value])
            return d

        heapq
        return max(profit + [max(dp())])


if __name__ == '__main__':
    startTime = [1,2,3,3]
    endTime = [3,4,5,6]
    profit = [50,10,40,70]

    assert len(startTime) == len(endTime) == len(profit), 'Invalid input parameters'

    res = Solution().jobScheduling(
        startTime=startTime,
        endTime=endTime,
        profit=profit,
    )
    print(res)
