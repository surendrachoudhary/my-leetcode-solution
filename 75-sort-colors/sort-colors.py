import collections

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 

        # Initialize a dictionary to count occurrences of each color
        num_dict = collections.defaultdict(int)
        n = len(nums)


        cnt0 = 0
        cnt1 = 0
        cnt2 = 0
        # Count occurrences of each color
        for i in nums:
            if i == 0:
                cnt0 += 1
            elif i == 1:
                cnt1 += 1
            else:
                cnt2 += 1

        # Replace the values in the original list with sorted colors
        for i in range(cnt0):
            nums[i] = 0

        for i in range(cnt0, cnt0 + cnt1):
            nums[i] = 1

        for i in range(cnt0 + cnt1, cnt0 + cnt1 + cnt2):
            nums[i] = 2
