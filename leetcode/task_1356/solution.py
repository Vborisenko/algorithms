from functools import cmp_to_key
from typing import List


class Solution:
    @classmethod
    def sortByBits(cls, arr: List[int]) -> List[int]:
        comparator = lambda a, b: 1 if cls.get_number_of_bits(a) > cls.get_number_of_bits(b)  \
            else -1 if cls.get_number_of_bits(a) < cls.get_number_of_bits(b) \
            else 1 if a > b else -1 if a < b else 0

        return list(sorted(arr, key=cmp_to_key(comparator)))

    @staticmethod
    def get_number_of_bits(number) -> int:
        return len(bin(number)[2:].replace('0', ''))


if __name__  == '__main__':
    Solution.sortByBits(arr=[2, 1, 3, 5, 7,8, 10])
