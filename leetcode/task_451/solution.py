from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(
            sorted(
                [key * value for key, value in Counter(list(s)).items()],
                key=lambda x: len(x), reverse=True
            )
        )

if __name__ == '__main__':
    Solution().frequencySort("bbbAaaCC")
