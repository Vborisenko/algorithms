from collections import Counter, defaultdict
from typing import List


class OldSolution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter_hash = Counter(arr)
        return counter_hash.most_common(1)[0][0]


class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        max_count = current_count = 0
        val = min(nums)

        for i in sorted(nums):
            if i == val:
                current_count += 1
            else:
                current_count = 1
                val = i

            max_count = current_count if max_count < current_count else max_count

            if max_count >= len(nums) // 2 + 1:
                return i


class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]


# Boyer–Moore Majority Vote
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for x in nums:
            if count == 0:
                candidate = x
                count = 1
            elif x == candidate:
                count += 1
            else:
                count -= 1

        return candidate

if __name__ == '__main__':
    inp = [3, 3, 3, 1, 1, 1, 1, 3, 3]
    Solution().majorityElement(inp)
