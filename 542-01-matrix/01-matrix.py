class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        direction = [(-1,0), (1,0), (0,1), (0,-1)]
        visited = set()

        q = deque([])


        result_matrix = [[0 for _ in range(cols)] for _ in range(rows)]


        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    q.append((row,col,0))
                    visited.add((row,col))

        while q:
            row, col, distance = q.popleft()
            total_dis = distance + 1
            for dx, dy in direction:
                nx, ny = row + dx, col + dy
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny)not in visited:
                    result_matrix[nx][ny] = total_dis
                    q.append((nx,ny,total_dis))
                    visited.add((nx,ny))

        return result_matrix



