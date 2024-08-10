class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        ROW1, COL1 = len(grid), len(grid[0])
        ROW2, COL2 = ROW1 * 3, COL1 * 3 
        grid2 = [[0] * COL2 for _ in range(ROW2)]

        for r in range(ROW1):
            for c in range(COL1):
                r2, c2 = r * 3, c * 3
                if grid[r][c] == "/":
                    grid2[r2][c2+2] = 1
                    grid2[r2+1][c2+1] = 1
                    grid2[r2+2][c2] = 1
                
                elif grid[r][c] == "\\":
                    grid2[r2][c2] = 1
                    grid2[r2+1][c2+1] = 1
                    grid2[r2+2][c2+2] = 1
        
        def dfs(r,c, visited):
            if not (0 <= r < ROW2) or not (0 <= c < COL2) or (r, c) in visited or grid2[r][c] != 0:
                return 
            visited.add((r,c))
            directions = [[r+1,c],[r,c+1],[r-1,c],[r,c-1]]

            for dr, dc in directions:
                dfs(dr, dc, visited)
                

        visited = set()
        result = 0
        for r in range(ROW2):
            for c in range(COL2):
                if (r,c) not in visited and grid2[r][c] == 0:
                    dfs(r,c ,visited)
                    result += 1

        return result 

