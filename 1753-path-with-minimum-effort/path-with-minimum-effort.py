class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        output = [[float('inf')] * cols for _ in range(rows)]
        
        pq = [(0,0,0)]
        
        output[0][0] = 0

        while pq:
            diff, row, col = heapq.heappop(pq)

            if row == rows -1 and col == cols -1:
                return diff 

            for dx, dy in directions:
                r, c = row+dx, col + dy
                if 0 <= r < rows and 0 <= c < cols:
                    new_diff = max(diff, abs(heights[r][c] - heights[row][col]))
                
                    if new_diff < output[r][c]:
                        heapq.heappush(pq, (new_diff, r, c))
                        output[r][c] = new_diff
            
        