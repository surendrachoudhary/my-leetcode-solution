# Using the Dutch National Flag problem to solve the question with a one-pass algorithm using only constant extra space
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Get the length of the input list
        n = len(nums)
        
        # Initialize three pointers: low, mid, and high
        low, mid = 0, 0
        high = n - 1

        # Loop until mid pointer crosses high pointer
        while mid <= high:
            # If the current element is 0, swap it with the element at low pointer
            if nums[mid] == 0:
                nums[mid], nums[low] = nums[low], nums[mid]
                mid += 1
                low += 1

            # If the current element is 1, move mid pointer forward
            elif nums[mid] == 1:
                mid += 1

            # If the current element is 2, swap it with the element at high pointer
            elif nums[mid] == 2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
