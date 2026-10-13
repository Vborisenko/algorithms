class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        mon_stack = deque()

        for i in range(len(heights)):
            while mon_stack and heights[mon_stack[-1]] > heights[i]:
                last_cand = mon_stack.pop()
                left = mon_stack[-1] if mon_stack else -1
                max_area = max(max_area, (heights[last_cand] * (i - left - 1)))

            if not mon_stack or heights[mon_stack[-1]] <= heights[i]:
                mon_stack.append(i)

        right = len(heights)
        while mon_stack:
            last_cand = mon_stack.pop()
            left = mon_stack[-1] if mon_stack else -1
            max_area = max(max_area, (heights[last_cand] * (right - left - 1)))

        return max_area