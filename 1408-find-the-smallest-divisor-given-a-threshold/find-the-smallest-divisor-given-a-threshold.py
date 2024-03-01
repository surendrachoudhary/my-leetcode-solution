class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # Function to check if a given divisor is valid
        def is_divisor(divisor):
            count = 0
            # Iterate through each number in nums and calculate the sum of divisions rounded up
            for dividend in nums:
                count += math.ceil(dividend / divisor)
            return count
        
        # Initialize the search range
        low, high = 1, max(nums)  # Start low from 1 and high from the maximum element in nums
        
        # Binary search to find the smallest divisor
        while low <= high:
            mid = (low + high) // 2  # Calculate the midpoint
            
            # Check if the current divisor satisfies the threshold
            if is_divisor(mid) <= threshold:
                high = mid - 1  # If yes, update high pointer to search for smaller divisors
            else:
                low = mid + 1  # If not, update low pointer to search for larger divisors
        
        return low  # Return the smallest divisor found
