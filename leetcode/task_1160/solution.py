from typing import List


class Solution:
    @staticmethod
    def countCharacters(words: List[str], chars: str) -> int:
        results = []

        for word in words:
            chars_list = list(chars)

            for letter in word:
                if letter in chars:
                    results.append(len(word))

        return int(sum(results))


if __name__ == '__main__':
    print(Solution.countCharacters(["hello","world","leetcode"], "welldonehoneyr"))
