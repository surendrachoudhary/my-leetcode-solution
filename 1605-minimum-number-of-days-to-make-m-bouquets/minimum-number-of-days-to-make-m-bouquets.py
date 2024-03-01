class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        # Function to count the number of bouquets that can be made on a given day
        def get_bouquets(day):
            adjacent_flowers = 0  # Counter for adjacent flowers
            bouquet = 0  # Counter for bouquets made
            for bloom in bloomDay:  # Iterate through the bloom days
                if bloom <= day:  # If the bloom day is less than or equal to the given day
                    adjacent_flowers += 1  # Increment the adjacent flowers counter
                else:
                    adjacent_flowers = 0  # Reset the adjacent flowers counter if not in bloom

                if adjacent_flowers == k:  # If enough adjacent flowers for a bouquet
                    bouquet += 1  # Increment the bouquet counter
                    adjacent_flowers = 0  # Reset the adjacent flowers counter

            return bouquet  # Return the total number of bouquets made

        low, high = 1, max(bloomDay)  # Set the low and high bounds for binary search

        while low <= high:  # Perform binary search
            mid = (low + high) // 2  # Calculate the middle day
            
            # If the number of bouquets made on this day is greater than or equal to the required m
            if get_bouquets(mid) >= m:
                high = mid - 1  # Update the upper bound
            else:
                low = mid + 1  # Update the lower bound

        # Return the result or -1 if no solution found within the bloom days
        return low if low <= max(bloomDay) else -1
