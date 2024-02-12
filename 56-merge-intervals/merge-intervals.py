class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the intervals based on their start times
        intervals = sorted(intervals)

        # Initialize an empty list to store the merged intervals
        ans = []

        # Iterate through each interval
        for interval in intervals:
            # If the merged list is empty or the current interval's start time is after the end time of the last merged interval
            if not ans or ans[-1][1] < interval[0]:
                # Add the current interval to the merged list
                ans.append(interval)
            else:
                # Update the end time of the last merged interval if there's an overlap
                ans[-1][1] = max(ans[-1][1], interval[1])
        
        # Return the merged intervals
        return ans
