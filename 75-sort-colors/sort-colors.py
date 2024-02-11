import collections

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 

        # Initialize a dictionary to count occurrences of each color
        num_dict = collections.defaultdict(int)
        n = len(nums)

        # Count occurrences of each color
        for i in nums:
            num_dict[i] += 1

        # Assign the counts to respective variables
        zero_val = num_dict[0]
        one_val = num_dict[1]
        two_val = num_dict[2]

        # Replace the values in the original list with sorted colors
        for i in range(zero_val):
            nums[i] = 0

        for i in range(zero_val, zero_val + one_val):
            nums[i] = 1

        for i in range(zero_val + one_val, zero_val + one_val + two_val):
            nums[i] = 2
