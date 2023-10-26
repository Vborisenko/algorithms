"""
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return False if n <= 0 else True if n == 1 else '1' not in bin(n)[3:] and not len(bin(n)[3:]) % 2
