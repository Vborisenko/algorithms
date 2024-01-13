class Solution:
    @classmethod
    def largestOddNumber(cls, num: str) -> str:
        slise_index = cls._get_first_odd_integer_index(num)
        return num[:slise_index] if slise_index else num if slise_index == 0 else ''

    @staticmethod
    def _get_first_odd_integer_index(num: str) -> int:
        index = 1

        for i in num[::-1]:
            if int(i) % 2:
                return -(index - 1)

            index += 1


if __name__ =='__main__':
    print(Solution.largestOddNumber(num='35427'))
