from collections import deque


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        result = float("inf")
        mon_stack = deque()
        prefix_sum = [0]
        for i in nums:
            prefix_sum.append(prefix_sum[-1] + i)

        for i in range(len(prefix_sum)):
            while mon_stack and (prefix_sum[i] - prefix_sum[mon_stack[0]]) >= k:
                result = min(result, i - mon_stack[0])
                mon_stack.popleft()

            while mon_stack and prefix_sum[mon_stack[-1]] > prefix_sum[i]:
                mon_stack.pop()
            mon_stack.append(i)

        return result if result != float("inf") else -1


if __name__ == '__main__':
    res = Solution().shortestSubarray([33,9,-4,95,-27,37,31,70,44,-30], 111)
    print(res)
