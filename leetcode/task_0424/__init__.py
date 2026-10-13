from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_counter = defaultdict(lambda: 0)
        i = j = current_max_freq = max_length = 0
        while j < len(s):
            window_size = j - i + 1
            freq_counter[s[j]] += 1
            current_max_freq = max(freq_counter[s[j]], current_max_freq)
            if window_size - current_max_freq > k:
                freq_counter[s[i]] -= 1
                i +=1
            else:
                max_length = max(window_size, max_length)
            j += 1
        return max_length


if __name__ == '__main__':
    s = "AABABBA"
    k = 1
    Solution().characterReplacement(s, k)

