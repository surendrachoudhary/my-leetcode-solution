class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image
        
        rows, cols = len(image), len(image[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque([(sr, sc)])
        image[sr][sc] = color
        
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and image[nx][ny] == original_color:
                    image[nx][ny] = color
                    q.append((nx, ny))
        
        return image
