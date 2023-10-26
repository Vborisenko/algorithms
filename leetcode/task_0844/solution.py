class Solution:
    @classmethod
    def backspaceCompare(cls, s: str, t: str) -> bool:
        return cls._get_string(s) == cls._get_string(t)

    @staticmethod
    def _get_string(string: str) -> str:
        processed_string, backspace_counter = [], 0

        for i in range(1, len(string) + 1):
            if string[-i] != '#' and not backspace_counter:
                processed_string.append(string[-i])
            elif string[-i] == '#':
                backspace_counter += 1
            else:
                backspace_counter -= 1

        return ''.join(list(reversed(processed_string)))


if __name__ == '__main__':
    print(Solution().backspaceCompare("ab##", "c#d#"))
