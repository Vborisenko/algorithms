from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        s_char_count = Counter(s)

        for ch, count in s_char_count.items():
            if count // 3:
                while count // 3:
                    count = count - (count // 3 * 2)
                s_char_count[ch] = count

        return sum(s_char_count.values())


if __name__ == '__main__':
    Solution().minimumLength(
        "ucvbutgkohgbcobqeyqwppbxqoynxeuuzouyvmydfhrprdbuzwqebwuiejoxsxdhbmuaiscalnteocghnlisxxawxgcjloevrdcj"
    )
