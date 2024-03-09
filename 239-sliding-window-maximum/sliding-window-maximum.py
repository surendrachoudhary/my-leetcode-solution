from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Length of the input array
        n = len(nums)

        # Initialize a deque to store indices
        queue = deque() 
        # Initialize a list to store the result
        result = []

        # Iterate through the array
        for i in range(n):
            # Remove indices from the deque if their corresponding elements are smaller than or equal to the current element
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()

            # Add the current index to the deque
            queue.append(i)

            # Remove indices that are out of the sliding window
            if queue[0] <= i - k:
                queue.popleft()

            # If we have processed at least k elements, append the maximum of the sliding window to the result
            if i >= k - 1:
                result.append(nums[queue[0]])

        return result
