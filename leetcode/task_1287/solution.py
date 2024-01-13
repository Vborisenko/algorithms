from collections import Counter, defaultdict
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter_hash = Counter(arr)
        return counter_hash.most_common(1)[0][0]


if __name__ == '__main__':
    Solution().findSpecialInteger([1,2,2,6,6,6,6,7,10])
