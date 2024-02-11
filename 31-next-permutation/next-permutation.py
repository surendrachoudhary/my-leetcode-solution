class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # Find the index of the first element from the right that breaks the descending order
        index = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                index = i
                break
        
        # If index remains -1, the array is in descending order, so reverse the entire array
        if index == -1:
            nums.reverse()
        else:
            # Find the rightmost element greater than the element at index
            for i in range(n-1, -1, -1):
                if nums[index] < nums[i]:
                    # Swap the two elements
                    nums[index], nums[i] = nums[i], nums[index]
                    break

            # Reverse the subarray from index+1 to the end
            left, right = index+1, n-1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
