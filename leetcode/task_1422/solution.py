class Solution:
    @classmethod
    def maxScore(cls, s: str) -> int:
        max_score = 0

        for i in range(1, len(s)):
            max_score = max(max_score, s[:i].count('0') + s[i:].count('1'))

        return max_score


if __name__ == '__main__':
    # string = str(input())
    string = '011101'

    assert len(string) >= 2, 'String is too short'
    assert not string.replace('1', '').replace('0', ''), 'String contains extra symbols'

    print(Solution.maxScore(string))
