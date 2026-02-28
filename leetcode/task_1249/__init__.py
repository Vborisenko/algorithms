class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_stack = []
        count = 0
        for i in range(len(s)):
            if s[i].isalpha():
                continue
            if s[i] == ")":
                count -= 1
                if count < 0:
                    indexes_stack.append(i)
                continue
            # s[i] == ')'
            if count < 0:
                count = 0
            count += 1

        s = list(s)
        for i in indexes_stack:
            s[i] = ""

        i = len(s) - 1
        while i >= 0 and count > 0:
            if s[i] == "(":
                s[i] = ""
                count -= 1
            i -= 1

        return "".join(s)
