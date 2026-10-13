from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q = deque()
        max_q = deque()
        result = 0

        for i in range(len(nums)):
            while min_q and nums[min_q[-1]] > nums[i]:
                min_q.pop()
            while max_q and nums[max_q[-1]] < nums[i]:
                max_q.pop()

            min_q.append(i)
            max_q.append(i)

            while nums[max_q[0]] - nums[min_q[0]] > limit:
                if max_q[0] > min_q[0]:
                    min_q.popleft()
                else:
                    max_q.popleft()

            if max_q and min_q:
                result = max(result, i - min(min_q[0], max_q[0]) + 1)

        return result


if __name__ == '__main__':
    nums = [10,4,5,3,1,2,4,7,2]
    limit = 5
    Solution().longestSubarray(nums, limit)
