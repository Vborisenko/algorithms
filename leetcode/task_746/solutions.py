from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        resul_sum = cost[:2]
        for i in cost[2:]:
            resul_sum.append(min(resul_sum[-2:] ) + i)
        return min(resul_sum[-2:])


if __name__ == '__main__':
    input_value = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    print(Solution().generate(input_value))
