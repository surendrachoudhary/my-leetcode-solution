from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, -1), (-1, 1), (1, 1)]

        output_2d = [[float('inf')] * cols for _ in range(rows)]
        if grid[0][0] != 0:
            return -1
            
        q = deque([(1,0,0)])
        output_2d[0][0] = 1

        while q:
            wei, row, col = q.popleft()

            for r, c in directions:
                nrow, ncol = row + r, col + c
                if 0 <= nrow < rows and 0 <= ncol < cols and grid[nrow][ncol] == 0:
                    new_wei = wei + 1
                    if new_wei < output_2d[nrow][ncol]:
                        output_2d[nrow][ncol] = new_wei
                        if nrow == rows-1 and ncol == cols-1:
                            break
                        q.append((new_wei, nrow, ncol))
        
        if output_2d[rows-1][cols-1] == float('inf'):
            return -1

        return output_2d[rows-1][cols-1]

