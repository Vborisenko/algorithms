from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        current_sum, new_list = 0, []

        for i in nums:
            current_sum  += i
            new_list.append(current_sum)

        return new_list

if __name__ == '__main__':
    input_val = [int(_) for _ in input().split()]
    print(Solution().runningSum(input_val))