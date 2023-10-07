class Solution:
    def reverse_words(self, s: str) -> str:
        return ' '.join(''.join((list(reversed(word)))) for word in s.split())


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse_words("Let's take LeetCode contest"))
