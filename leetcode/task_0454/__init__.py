"""
454. 4Sum II

Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
"""
from typing import List, Dict, Tuple


class Solution:
    @staticmethod
    def get_counter(array: List) -> Dict:
        counter = dict()
        for i in array:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        return counter

    @staticmethod
    def get_pairs(arr1: List, arr2: List) -> List[Tuple]:
        arr1, arr2 = list(arr1), list(arr2)
        pairs = list()

        for i in range(len(arr1)):
            for j in range(len(arr2)):
                pairs.append((arr1[i], arr2[j]))
        return pairs

    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        counter1 = self.get_counter(nums1)
        counter2 = self.get_counter(nums2)
        counter3 = self.get_counter(nums3)
        counter4 = self.get_counter(nums4)
        pairs1_2 = self.get_pairs(counter1.keys(), counter2.keys())
        pairs3_4 = self.get_pairs(counter3.keys(), counter4.keys())

        # note: pairs contains different lengths
        def get_sum_map(pairs: List, counter_1, counter_2):
            sum_map = {}
            for pair in pairs:
                if sum(pair) in sum_map:
                    sum_map[sum(pair)] += counter_1[pair[0]] * counter_2[pair[1]]
                else:
                    sum_map[sum(pair)] = counter_1[pair[0]] * counter_2[pair[1]]
            return sum_map

        pairs_sum_map1 = get_sum_map(pairs1_2, counter1, counter2)
        pairs_sum_map2 = get_sum_map(pairs3_4, counter3, counter4)
        total_sum = 0
        for sum_, pairs_list in pairs_sum_map1.items():
            if -sum_ in pairs_sum_map2:
                total_sum += pairs_sum_map1[sum_] * pairs_sum_map2[-sum_]

        return total_sum


if __name__ == '__main__':
    nums1 = [12, -7, 3, 18, -15, 0, 9, -4, 21, -10, 6, -2, 14, -18, 5, -1]
    nums2 = [-5, 8, -12, 4, 16, -3, 0, -9, 11, -14, 2, 7, -6, 19, -1, -17]
    nums3 = [10, -8, -4, 15, -20, 6, 1, -11, 13, -2, 0, 9, -7, 18, -5, 3]
    nums4 = [-17, 5, 9, -6, 2, -14, 8, 0, -3, 11, -10, 16, -1, 4, -9, 7]
    # nums1 = [0]
    # nums2 = [0]
    # nums3 = [0]
    # nums4 = [0]

    Solution().fourSumCount(nums1, nums2, nums3, nums4)

