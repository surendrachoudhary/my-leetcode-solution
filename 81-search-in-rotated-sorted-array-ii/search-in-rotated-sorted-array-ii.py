class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Initialize pointers for binary search
        low, high = 0, len(nums) - 1

        # Perform binary search until low pointer is less than or equal to high pointer
        while low <= high:
            # Calculate mid index
            mid = (low + high) // 2

            # Check if target is found at mid index
            if target == nums[mid]:
                return True 
            
            # Handle the case where there are duplicates at the boundaries
            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                # Move pointers inward to skip duplicate elements
                low += 1
                high -= 1
                continue

            # Check if left half is sorted
            if nums[mid] >= nums[low]:
                # If target is within the sorted left half, update high pointer
                if target <= nums[mid] and target >= nums[low]:
                    high = mid - 1 
                # Otherwise, update low pointer
                else:
                    low = mid + 1
            else:
                # If target is within the right half, update low pointer
                if target >= nums[mid] and target <= nums[high]:
                    low = mid + 1
                # Otherwise, update high pointer
                else:
                    high = mid - 1 
        
        # Target not found in the array
        return False
