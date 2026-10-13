import heapq


class Solution1:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        counter = 0
        for x, y in points:
            heap.append((x ** 2 + y ** 2, counter, [x, y]))
            counter += 1
        heapq.heapify(heap)

        results=[]
        for _ in range(k):
            _, _, coordinates = heapq.heappop(heap)
            results.append(coordinates)
        return results


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        counter = 0
        for x, y in points:
            if len(heap) < k:
                heapq.heappush_max(heap, (x**2 + y**2, counter, [x, y]))
            else:
                heapq.heappushpop_max(heap, (x**2 + y**2, counter, [x, y]))
            counter += 1
        return [coords for _, _, coords in heap]



if __name__ == "__main__":
    res = Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2)
    print(res)
