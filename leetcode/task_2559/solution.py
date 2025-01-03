from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel_letters = 'aeiou'
        words_indicator = [1 if word[0] in vowel_letters and word[-1] in vowel_letters else 0 for word in words]
        prefix_sum = [words_indicator[0]] * len(words_indicator)

        for i in range(1, len(words_indicator)):
            prefix_sum[i] = words_indicator[i] + prefix_sum[i-1]

        final_list = [prefix_sum[y] - prefix_sum[x-1] if x > 0 else prefix_sum[y] for x, y in queries]

        return final_list


if __name__ == '__main__':
    words = ["aba", "bcb", "ece", "aa", "e"]
    q = [[0, 2], [1, 4], [1, 1]]
    Solution().vowelStrings(words, q)
