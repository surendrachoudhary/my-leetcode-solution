class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(row,col, visited):
            if not (0 <= row < rows) or not (0 <= col < cols) or (grid[row][col] == 0) or (row,col) in visited:
                return 
            visited.add((row,col))
            directions = [[row+1, col], [row, col+1],[row-1, col],[row, col-1],]

            for dr, dc in directions:
                dfs(dr,dc, visited)
        dfs_call = 0
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] != 0) and (r,c) not in visited:
                    dfs(r,c,visited)
                    dfs_call += 1
        
        if dfs_call != 1:
            return 0

        visited_list = list(visited)

        for ro,co in visited_list:
            grid[ro][co] = 0

            dfs_call = 0
            visited = set()
            for r in range(rows):
                for c in range(cols):
                    if (grid[r][c] != 0) and (r,c) not in visited:
                        dfs(r,c,visited)
                        dfs_call += 1
            if dfs_call != 1:
                return 1
            
            grid[ro][co] = 1
        
        return 2

