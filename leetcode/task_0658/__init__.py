class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for i in range(len(arr)):
            if len(heap) < k:
                heapq.heappush(heap, (-abs(arr[i] - x), -arr[i], i))
            else:
                heapq.heappushpop(heap, (-abs(arr[i] - x), -arr[i], i))
        results = [i for _, _, i in heap]
        return [arr[i] for i in sorted(results)]
