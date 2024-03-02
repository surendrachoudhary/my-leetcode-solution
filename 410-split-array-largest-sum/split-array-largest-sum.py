class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Initialize low and high bounds
        low = max(nums)
        high = sum(nums)

        # Function to find the minimum sum required for the given number of splits
        def find_mini_sum(sum_val):
            split_num = 1
            capacity = 0

            # Iterate through the array to calculate splits
            for i in nums:
                # If the current capacity plus the current number is less than or equal to the sum value
                # increment the capacity
                if capacity + i <= sum_val:
                    capacity += i
                # If the current capacity plus the current number exceeds the sum value,
                # increment the split number and reset the capacity to the current number
                else:
                    split_num += 1
                    capacity = i

            return split_num

        # Perform binary search to find the minimum sum that satisfies the conditions
        while low <= high:
            mid = (low + high) // 2

            # If the current minimum sum is valid for the given number of splits,
            # update the high bound
            if find_mini_sum(mid) <= k:
                high = mid - 1
            # If the current minimum sum is not valid for the given number of splits,
            # update the low bound
            else:
                low = mid + 1

        return low
