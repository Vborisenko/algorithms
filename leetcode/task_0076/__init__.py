from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        t = "abccdd"
        s = "aabbreccasdd"

        It's possible to create a counter for t and go through the s with L-R sliding window.
        The only issue is in comparing the t-string counter and current L-R counter by t-counter keys.
        We will also initialize 2 metrics:
        required_count = value of unique symbols quantoty in t string.
        current_count = value of unique symbols quantity in window with enough window_counter[i].
        s_key_count should be incremented, if we have window_counter[s[r]] == t_counter[s[r]].
        if current_count == required_count, then the window is correct and we can move the L-boundary,
        till the window_counter[s[l]] = t_counter[s[l]]. It's a signal for count the min_length
        (because s[l] in this case is the 1st window element).
        min_length = min(min_length, r - l + 1)
        """
        if len(t) > len(s):
            return ""

        t_counter = defaultdict(lambda: 0)
        for _ in t:
            t_counter[_] += 1

        l = r = 0
        window_counter = defaultdict(lambda: 0)
        required_count = len(t_counter.keys())
        current_count = 0
        boundaries = [float("-inf"), float("inf")]

        while r < len(s):
            if s[r] in t_counter:
                window_counter[s[r]] += 1
                if window_counter[s[r]] == t_counter[s[r]]:
                    current_count += 1
                if current_count == required_count:
                    while s[l] not in t_counter or window_counter[s[l]] > t_counter[s[l]]:
                        if s[l] in t_counter:
                            window_counter[s[l]] -= 1
                        l += 1
                    if r - l < boundaries[1] - boundaries[0]:
                        boundaries[0], boundaries[1]  = l, r
            r += 1
        return s[boundaries[0] : boundaries[1] + 1]

if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    Solution().minWindow(s, t)