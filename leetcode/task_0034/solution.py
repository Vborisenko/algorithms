from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int):
        if not nums or nums[0] > target or nums[-1] < target:
            return [-1, -1]

        target_left_index = self.find_target_index(nums, target)

        if target_left_index is None:
            return [-1, -1]

        while nums[target_left_index] == target and target_left_index >= 0:
            if target_left_index == 0:
                break
            elif nums[target_left_index - 1] == target:
                target_left_index -= 1
            else:
                break

        target_right_index = target_left_index

        while nums[target_right_index] == target:
            if len(nums) -1 <= target_right_index:
                break
            elif nums[target_right_index + 1] == target:
                target_right_index += 1
            else:
                break

        return [target_left_index, target_right_index]

    @staticmethod
    def find_target_index(nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return None


if __name__ == '__main__':
    print(Solution().searchRange([1,2,3,3,3,3,4,5,9], 3))
