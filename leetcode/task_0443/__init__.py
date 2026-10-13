class Solution:
    def compress(self, chars: List[str]) -> int:
        char_counter = r = 1
        l = 0
        while r <= len(chars) - 1:
            if chars[r] == chars[r-1]:
                char_counter += 1
                r += 1
            else:
                l = self._calculate(chars, l, r, char_counter)
                r += 1
                char_counter = 1
        return self._calculate(chars, l, r, char_counter)

    @staticmethod
    def _calculate(chars: List[str], l: int, r: int, char_counter: int) -> int:
        chars[l] = chars[r-1]
        l += 1
        if char_counter > 1:
            for i in str(char_counter):
                chars[l] = i
                l += 1
        return l
