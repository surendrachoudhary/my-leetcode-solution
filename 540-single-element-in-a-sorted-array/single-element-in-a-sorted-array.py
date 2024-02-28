class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Get the length of the nums list
        n = len(nums)
        
        # If there's only one element in the list, it's the single non-duplicate element
        if n == 1:
            return nums[0]
        
        # Check if the single non-duplicate element is the first element
        if nums[0] != nums[1]: 
            return nums[0]
        
        # Check if the single non-duplicate element is the last element
        if nums[n-1] != nums[n-2]: 
            return nums[n-1]
        
        # Binary search part
        start, end = 1, n-2

        while start <= end:
            # Calculate the midpoint
            mid = (start + end) // 2
            
            # Check if nums[mid] is the single non-duplicate element
            if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return nums[mid]
            
            # Adjust start and end pointers based on the position of nums[mid] and its adjacent elements
            elif mid % 2 == 1 and nums[mid] == nums[mid-1] or mid % 2 == 0 and nums[mid] == nums[mid+1]:
                start = mid+1
            else:
                end = mid-1
