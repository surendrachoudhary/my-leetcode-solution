class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Function to calculate the total hours needed to eat all bananas with given speed
        def get_hour(per_hour):
            hour_count = 0
            for bananas in piles:
                hour_count += math.ceil(bananas/per_hour)  # Calculate hours needed for each pile and accumulate
            return hour_count

        # Initialize low and high pointers for binary search
        low, high = 1, max(piles)  # Start low from 0 and high from the maximum pile size
        
        # Perform binary search to find the minimum eating speed
        while low <= high:
            mid = (low + high) // 2  # Calculate the midpoint
            
            # Check if the total hours needed with the current speed is less than or equal to available hours
            if get_hour(mid) <= h:
                high = mid - 1  # If yes, update high pointer to search for smaller speeds
            else:
                low = mid + 1  # If not, update low pointer to search for higher speeds
        
        return low  # Return the minimum eating speed found
