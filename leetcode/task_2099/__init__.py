class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        heap = []
        for i in range(len(nums)):
            heapq.heappush_max(heap, (nums[i], i))
        subsequence_idx = []
        for _ in range(k):
            val, idx = heapq.heappop_max(heap)
            subsequence_idx.append(idx)
        subsequence_idx.sort()
        return [nums[i] for i in subsequence_idx]