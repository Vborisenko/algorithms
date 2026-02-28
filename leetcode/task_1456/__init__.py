class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        current_count = len([i for i in s[:k] if i in vowels])
        max_count = current_count

        j = 0
        for i in range(k, len(s)):
            if s[j] in vowels:
                current_count -= 1
            if s[i] in vowels:
                current_count += 1

            max_count = max(max_count, current_count)
            j += 1

        return max_count
