"""
1658. Minimum Operations to Reduce X to Zero

You are given an integer array nums and an integer x.
In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x.
Note that this modifies the array for future operations.
Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

Example 1:
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

Example 2:
Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: The optimal solution is to remove the last three elements and the first two elements (5 operations in total) to reduce x to zero.
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        """
        1) If we build 2 prefix soms (from 0 to i, and from i to 0), we can easly find a sum of
        right- and left-side elements. The count of the elements is the answer of the question.

        E.g.:
        nums = [2, 3, 1, 4, 0, 1, 6, 2, 2, 1, 3, 0], x = 8
        pref_sum = [2, 5, 6, 10, 10, 11, 17]
        sum(nums[0] + ... nums[i] ) == nums[i] + pref_sum[i -]
        pref_sum1 = [2, 5, 6, 10]
        pref_sum2 = [0, 3, 4, 6, 8]


        it means there're 2 ways to get 8:
        1) [0, 1, -1, -2] indexes == 4 operations
        2) [-1, -2, ..., -5] indexes == 5 operations

        Based on it, we have the following invariant, if we want to calculate min operations (if it exists):
        a) If the i-th element of prefix sum is smaller than x -> we need to add elements from the end of another prefix_sum
        b) There could be 1 right case for each i-th: i == x or i + j == x, where j is a prefix_sum2 index from the end
        c) i = len(nums) - j - 1
           i + 1 = len(nums) - j
        d)
        """

        if sum(nums) < x:
            return -1
        if sum(nums) == x:
            return len(nums)

        pref_sum1, pref_sum2 = [0], [0]

        for i in range(len(nums)):
            pref_sum1.append(pref_sum1[i] + nums[i])
            pref_sum2.append(pref_sum2[i] + nums[-i - 1])

        result = float("inf")
        j = -1

        for i in range(len(pref_sum1)):
            while pref_sum1[i] + pref_sum2[j] > x and -j < len(pref_sum2) :
                j -= 1
            if pref_sum1[i] + pref_sum2[j] == x:
                result = min(result, i + len(pref_sum2) + j)

        return result if result != float("inf") else -1


if __name__ == '__main__':
    nums = [1,1,4,2,3]
    x = 5
    Solution().minOperations(nums, x)

    [1, 2, 3, 4]
    [5, 4, 3, 2, 1]