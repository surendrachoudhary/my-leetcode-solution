class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        directions = [(1,0), (-1,0), (0,1), (0, -1)]
        visited = set()

        # Visit the first row
        for col in range(cols):
            if grid[0][col] == 1:
                grid[0][col] = 2
                queue.append((0,col))
                visited.add((0,col))

        # Visit the last column
        for row in range(1, rows):
            if grid[row][cols - 1] == 1:
                grid[row][cols - 1] = 2
                queue.append((row, cols -1))
                visited.add((row, cols -1))


        # Visit the last row (if there are more than one row)
        if rows > 1:
            for col in range(cols - 2, -1, -1):
                if grid[rows - 1][col] == 1:
                    grid[rows - 1][col] = 2
                    queue.append((rows-1, col))
                    visited.add((rows-1, col))

        # Visit the first column (if there are more than one column)
        if cols > 1:
            for row in range(rows - 2, 0, -1):
                if grid[row][0] == 1:
                    grid[row][0] = 2
                    queue.append((row, 0))
                    visited.add((row, 0))

        while queue:
            row, col = queue.popleft()

            for dx, dy in directions:
                r, c = row + dx, col + dy

                if (r,c) not in visited and 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                    grid[r][c] =  2
                    queue.append((r,c))
                    visited.add((r,c))

        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    count += 1

        return count 

