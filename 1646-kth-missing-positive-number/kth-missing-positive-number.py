class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Initialize low and high pointers
        low = 0
        high = len(arr) - 1
        
        # Binary search loop
        while low <= high:
            # Calculate mid index
            mid = (low + high) // 2
            
            # Calculate the number of missing integers before arr[mid]
            missing = arr[mid] - (mid + 1)
            
            # Adjust low and high pointers based on missing count
            if missing < k:
                low = mid + 1
            else:
                high = mid - 1
        
        # Return the k-th missing positive integer
        return k + high + 1
