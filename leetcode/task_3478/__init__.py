class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        nums1_heap = []
        for i in range(len(nums1)):
            heapq.heappush(nums1_heap, (nums1[i], i))
        result = [0] * len(nums1)
        last_value, last_idx = heapq.heappop(nums1_heap)
        nums2_heap, current_sum = [], 0
        last_identical_group = []
        while nums1_heap:
            current_val, current_idx = heapq.heappop(nums1_heap)
            if current_val > last_value:
                while last_identical_group:
                    i = last_identical_group.pop()
                    if len(nums2_heap) < k:
                        current_sum += nums2[i]
                        heapq.heappush(nums2_heap, nums2[i])
                    elif nums2[i] > nums2_heap[0]:
                        removed = heapq.heappushpop(nums2_heap, nums2[i])
                        current_sum = current_sum - removed + nums2[i]
                if len(nums2_heap) < k:
                    current_sum += nums2[last_idx]
                    heapq.heappush(nums2_heap, nums2[last_idx])
                else:
                    if nums2[last_idx] > nums2_heap[0]:
                        removed = heapq.heappushpop(nums2_heap, nums2[last_idx])
                        current_sum = current_sum - removed + nums2[last_idx]
            else:
                 last_identical_group.append(last_idx)
            result[current_idx] = current_sum
            last_value = current_val
            last_idx = current_idx
        return result
