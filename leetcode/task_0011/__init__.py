class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        1) Result is product of min(height[i], height[j]) and j-i
        res = max(min(height[i], height[j]) * (j - i), max_water)
        """
        max_water = 0
        i, j = 0, len(height) - 1
        while i < j:
            max_water = max(min(height[i], height[j]) * abs(j - i), max_water)
            if height[j] < height[i]:
                j -= 1
            else:
                i += 1
        return max_water

