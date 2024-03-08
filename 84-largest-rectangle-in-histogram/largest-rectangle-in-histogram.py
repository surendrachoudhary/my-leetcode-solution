class Solution:
    def largestRectangleArea(self, bars: List[int]) -> int:
        # Get the number of bars
        n = len(bars)
        
        # Initialize an empty stack and arrays to store the indices of the nearest smaller bars
        stack = []
        left_smaller = [0] * n
        right_smaller = [0] * n
        
        # Variable to store the maximum area
        max_val = 0
        
        # Calculate the nearest smaller bar to the left of each bar
        for i in range(n):
            while stack and bars[stack[-1]] >= bars[i]:
                stack.pop()
            
            if not stack:
                left_smaller[i] = 0
                stack.append(i)
            else:
                left_smaller[i] = stack[-1] + 1
                stack.append(i)
        
        # Clear the stack
        stack = []
        
        # Calculate the nearest smaller bar to the right of each bar
        for i in range(n - 1, -1, -1):
            while stack and bars[stack[-1]] >= bars[i]:
                stack.pop()
            
            if not stack:
                right_smaller[i] = n - 1
                stack.append(i)
            else:
                right_smaller[i] = stack[-1] - 1
                stack.append(i)
        
        # Calculate the maximum area by iterating through each bar
        for i in range(n):
            max_val = max(max_val, (right_smaller[i] - left_smaller[i] + 1) * bars[i])
        
        return max_val
