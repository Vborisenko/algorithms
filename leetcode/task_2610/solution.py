from collections import defaultdict
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        hash_matrix = defaultdict(lambda: 0)

        for i in nums:
            hash_matrix[i] += 1

        result_list = [[] for _ in range(max(hash_matrix.values()))]

        for element, count in hash_matrix.items():
            i = 0
            while i < count:
                result_list[i].append(element)
                i += 1

        return result_list




if __name__ =='__main__':
    print(Solution().findMatrix(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 1, 4]))
