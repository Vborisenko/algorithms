class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        1) Create results array with len(temperatures) and values 0 to avoid post-processing of the array.
        2)Iterate through the temperatures array and collect elements indexes in a monotonic stack
        with ascending from head to tail.
        If i-th element is greater than mon. stack head — it's required to make pop last index from stack
        to store i-th value in results[j], where j-th is a stack[-1] (head).
        """
        n = len(temperatures)
        results = [0] * n
        mon_stack = []
        for i in range(n):
            while mon_stack and temperatures[mon_stack[-1]] < temperatures[i]:
                j = mon_stack.pop()
                results[j] = i - j
            mon_stack.append(i)
        return results