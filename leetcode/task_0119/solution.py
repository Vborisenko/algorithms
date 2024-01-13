from typing import List


class Solution:
    def getRow(self, row_index: int) -> List[int]:
        if row_index == 0:
            return [1]

        if row_index == 1:
            return [1, 1]

        array = [[1], [1, 1]]
        element_counter = 3

        for i in range(2, row_index + 1):
            row_array = [1]

            for j in range(1, element_counter - 1):
                row_array.append(array[i - 1][j - 1] + array[i - 1][j])

            row_array.append(1)
            array.append(row_array)
            element_counter += 1

        return row_array


if __name__ == '__main__':
    print(Solution().getRow(33))
