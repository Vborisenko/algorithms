"""
1711. Count Good Meals

A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.
You can pick any two different foods to make a good meal.
Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i-th item of food,
return the number of different good meals you can make from this list modulo 109 + 7.
Note that items with different indices are considered different even if they have the same deliciousness value.

Example 1:

Input: deliciousness = [1,3,5,7,9]
Output: 4
Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.
Example 2:

Input: deliciousness = [1,1,1,3,3,3,7]
Output: 15
Explanation: The good meals are (1,1) with 3 ways, (1,3) with 9 ways, and (1,7) with 3 ways.
"""
from collections import defaultdict
from typing import List


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 1000000007
        counter_freq = defaultdict(lambda: 0)
        counter = 0
        max_power = max(deliciousness) * 2

        for x in deliciousness:
            power = 1
            while power <= max_power:
                if counter_freq[power - x]:
                    counter += counter_freq[power - x]
                power *= 2
            counter_freq[x] += 1
            counter %= MOD

        return counter


if __name__ == '__main__':
    dels = [1,3,1,3,1,3,7]
    Solution().countPairs(dels)