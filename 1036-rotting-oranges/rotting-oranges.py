from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Initialize a queue to store the rotten oranges and other variables
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        max_minute = 0

        # Add the positions of all rotten oranges to the queue
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append(((i,j),0))

        # Perform BFS until the queue is empty
        while queue:
            index, minute = queue.popleft()
            max_minute = max(max_minute, minute)
            r = index[0]
            c = index[1]
            
            # Check left
            if c-1 >= 0 and grid[r][c-1] == 1:
                grid[r][c-1] = 2                
                queue.append(((r,c-1),minute+1))
            
            # Check right
            if c+1 < cols and grid[r][c+1] == 1:
                grid[r][c+1] = 2
                queue.append(((r,c+1),minute+1))

            # Check top
            if r-1 >= 0 and grid[r-1][c] == 1:
                grid[r-1][c] = 2
                queue.append(((r-1,c),minute+1))

            # Check bottom
            if r+1 < rows and grid[r+1][c] == 1:
                grid[r+1][c] = 2
                queue.append(((r+1,c),minute+1))

        # Check if there are any fresh oranges left
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1

        # Return the time taken for all oranges to become rotten
        return max_minute
