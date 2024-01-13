from typing import List


class Solution:
    @staticmethod
    def maxWidthOfVerticalArea(points: List[List[int]]) -> int:
        sorted_points = sorted(points)
        max_width = 0

        for i in range(len(sorted_points) - 1):
            if sorted_points[i + 1][0] - sorted_points[i][0] > max_width:
                max_width = sorted_points[i + 1][0] - sorted_points[i][0]

        return max_width


if __name__ == '__main__':
    Solution.maxWidthOfVerticalArea([[8,7],[9,9],[7,4],[9,7]])