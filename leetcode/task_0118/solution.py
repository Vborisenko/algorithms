from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row_num in range(numRows):
            row = [1] * (row_num + 1)
            for j in range(1, row_num):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            triangle.append(row)

        return triangle


if __name__ == '__main__':
    input_value = 5
    print(Solution().generate(input_value))
