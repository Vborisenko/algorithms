import heapq
from collections import Counter
from typing import List
from heapq import heapify, heappush, heappop, heappushpop


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_heap = [(-count, word) for word, count in Counter(words).items()]
        heapify(words_heap)
        return [heappop(words_heap)[1] for _ in range(k)]

if __name__ == '__main__':
    words, k = ["i","love","leetcode","i","love","coding"], 3
    Solution().topKFrequent(words, k)
