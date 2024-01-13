from typing import List


class Solution:
    @classmethod
    def sortByBits(cls, arr: List[int]) -> List[int]:
        return list(sorted(arr, key=lambda x: [bin(x).count('1'), x]))
