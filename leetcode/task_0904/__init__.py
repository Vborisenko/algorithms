from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        There're possibly 2 or 3 ways to resolve this task.

        1) We can generate fruit_types = [0]*leng(fruits) and loop through the array and increament the fruit_types[fruits[i]] with 1.
        E.g.:
        fruits      = [1, 2, 3, 2, 3, 1, 1, 3]
        fruit_types = [0, 3, 2, 3, 0, 0, 0, 0]

        Idk the possible solutuon using the indeces bucket of frut length elements

        2) The 2nd way to solve this task is 2 pointers.
        We have 2 trackers with current types of fruits. tracker_1 and tracker_2. Also we have R-th and L-th pointers.
        We can loop for R-th element through the fruits.
        And if the R-th elemnt is equal of one of the trackers we can proceed till the fruit[r] is not in (tracker_1, tracker_2).
        At this point of time we have to calculate the max_length of the arrange: max_length = max(r - l, max_length).
        The tracker_1 = fruits[r], and the tracker_2 = fruits[r - 1].
        Also we have to move the l till fruits[l] == tracker_

        3) Hash table approach:
        to be continued...
        """
        tracker_2 = None
        tracker_1 = fruits[0]
        max_length = l = 0
        for r in range(len(fruits)):
            if tracker_2 is None and fruits[r] != tracker_1:
                tracker_2 = fruits[r]

            if fruits[r] not in (tracker_1, tracker_2):
                max_length = max(max_length, r - l)
                tracker_1 = fruits[r - 1]
                tracker_2 = fruits[r]
                while fruits[l] !=  tracker_1:
                    l += 1
                continue

        return max(max_length, r - l + 1)


if __name__ == '__main__':
    fruits = [3,3,3,1,2,1,1,2,3,3,4]
    Solution().totalFruit(fruits)