class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Function to check if given weight capacity is feasible for shipping within given days
        def is_days(weight, start=0):
            t_weight = 0  # Total weight loaded on the current day
            days_count = 0  # Total days required for shipping
            
            # Iterate through the weights
            for val in range(len(weights)):
                t_weight += weights[val]  # Add the weight of the current package to the total
                
                # Check if adding the next package exceeds the weight capacity or it's the last package
                if val == len(weights) - 1 or t_weight + weights[val + 1] > weight:
                    days_count += math.ceil(t_weight / weight)  # Update days_count based on the current total weight
                    t_weight = 0  # Reset the total weight for the next day
                    
            return days_count
        
        # Set the lower bound of weight capacity to the maximum weight among the packages
        low, high = max(weights), sum(weights)  # Start from 1 and go up to the sum of all weights
        
        # Binary search to find the minimum ship's capacity
        while low <= high:
            mid = (low + high) // 2  # Calculate the mid capacity
            
            # If the capacity is feasible for shipping within given days, search in the lower half
            if is_days(mid) <= days:
                high = mid - 1 
            else:
                low = mid + 1  # Otherwise, search in the higher half
        
        return low  # Return the minimum ship's capacity found
