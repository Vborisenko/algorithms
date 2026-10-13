"""We can achieve the median counting by keeping 2 priority queue.

Size of active elements in both heaps should be the same or at least differ on 1.
Active element is the element with index from the current window (right - left + 1 = k).
We need also 2 current counters for the heaps' lengths.
Also to be able to update the counters while moving the left, we need to create a hash map, with a key as nums idexes, and value as 1 or 2 (heap number, also could be heap id).
Before counting the median, we need to be sure that the head of the both heaps have active elements (left <= i <= right).

The heaps structure is: [(val, idx), ...].
"""
import heapq


class Solution:
    def __init__(self):
        # heap1 is a heap for lower side of elements,
        # wether heap2 is an upper side of elements.
        # heap1 is collecting upside elements (mult. -1) to keep it as max heap,
        # wether heap2 is standart python min heap.
        # heap1[0] <= heap2[0]
        self.heap1, self.heap2 = [], []
        self.counter1 = self.counter2 = 0
        self.nums_map = {}

    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        self.nums_status = [1] * len(nums)
        for i in range(k):
            self._insert_new_element(nums[i], i)

        result = [self._count_midean()]
        left = 0

        for right in range(k, len(nums)):
            # move left and mark previous element as deactiovated
            self.nums_status[left] = 0
            if self.nums_map.get(left, None) and self.nums_map[left] == 1:
                self.counter1 -= 1
            else:
                self.counter2 -= 1
            left += 1
            self._insert_new_element(nums[right], right)
            result.append(self._count_midean())
        return result

    def _insert_new_element(self, num: int, idx: int) -> None:
        def swap_elements():
            (val1, idx1), (val2, idx2) = heapq.heappop(self.heap1), heapq.heappop(self.heap2)
            heapq.heappush(self.heap2, (-val1, idx1))
            heapq.heappush(self.heap1, (-val2, idx2))
            self.nums_map[idx1] = 2
            self.nums_map[idx2] = 1

        if self.counter1 == self.counter2:
            if not self.heap1 or not self.heap2:
                heapq.heappush(self.heap1, (-num, idx))
                self.counter1 += 1
            elif num < self.heap2[0][0]:
                heapq.heappush(self.heap1, (-num, idx))
                self.counter1 += 1
            else:
                heapq.heappush(self.heap2, (num, idx))
                self.counter2 += 1

        elif self.counter1 < self.counter2:
            heapq.heappush(self.heap1, (-num, idx))
            self.counter1 += 1
        else:
            heapq.heappush(self.heap2, (num, idx))
            self.counter2 += 1

        if self.heap1 and self.heap2 and -self.heap1[0][0] > self.heap2[0][0]:
            swap_elements()

        self._normilise_heads()
        if self.heap1:
            self.nums_map[self.heap1[0][1]] = 1
        if self.heap2:
            self.nums_map[self.heap2[0][1]] = 2

    def _normilise_heads(self):
        while self.heap1 and self.nums_status[self.heap1[0][1]] == 0:
            heapq.heappop(self.heap1)
        while self.heap2 and self.nums_status[self.heap2[0][1]] == 0:
            heapq.heappop(self.heap2)

    def _count_midean(self):
        if self.counter1 == self.counter2:
            return (-self.heap1[0][0] + self.heap2[0][0]) / 2
        elif self.counter1 > self.counter2:
            return -self.heap1[0][0]
        else:
            return self.heap2[0][0]


if __name__ == '__main__':
    nums = [4,1,7,1,8,7,8,7,7,4]
    k = 4
    res = Solution().medianSlidingWindow(nums, k)
    print(res)