class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        """
        The task can be solved using 2 monotonic queues.
        The first one, max_queue, stores indices of candidates for the maximum element in the current window.
        The values at these indices are kept in decreasing order, so the current maximum is always at the front of the queue.
        The second one, min_queue, stores indices of candidates for the minimum element in the current window.
        The values at these indices are kept in increasing order, so the current minimum is always at the front of the queue.

        We iterate through the array using a sliding window. For each right index, we add nums[right] to both queues
            while preserving their monotonic invariants.
        Then, while the current window is invalid, meaning: `nums[max_queue[0]] - nums[min_queue[0]] > 2`,
            we move left to the right and remove outdated indices from the fronts of the queues.

        After the window becomes valid, all subarrays ending at right and starting anywhere from left to right are valid.
        Therefore, we update the answer with: `result += right - left + 1`
        """
        min_dq, max_dq = deque(), deque()

        result = left = 0
        for right in range(len(nums)):
            while max_dq and nums[max_dq[-1]] < nums[right]: max_dq.pop()
            while min_dq and nums[min_dq[-1]] > nums[right]: min_dq.pop()
            max_dq.append(right)
            min_dq.append(right)

            while nums[max_dq[0]] - nums[min_dq[0]] > 2:
                if max_dq[0] == left:
                    max_dq.popleft()
                if min_dq[0] == left:
                    min_dq.popleft()
                left += 1

            result += right - left + 1

        return result