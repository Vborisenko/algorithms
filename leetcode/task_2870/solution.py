from collections import defaultdict
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hash_table = defaultdict(lambda: 0)

        for element in nums:
            hash_table[element] += 1

        if 1 in hash_table.values():
            return -1

        result = 0

        for value in hash_table.values():
            result += value // 3 + 1 if value % 3 else value // 3

        return result




if __name__ == '__main__':
    Solution().minOperations([2,3,3,2,2,4,2,3,4])
