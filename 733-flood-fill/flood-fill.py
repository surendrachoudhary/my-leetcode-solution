class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        st_color = image[sr][sc]
        
        if st_color == color:
            return image 

        visited = set()
        q = deque()
        q.append((sr,sc))
        image[sr][sc] = color 
        visited.add((sr,sc))
        
        while q:
            sr,sc = q.popleft()
            
            if sr-1 >= 0 and (sr-1,sc) not in visited and image[sr-1][sc] == st_color:
                image[sr-1][sc] = color 
                visited.add((sr-1,sc))
                q.append((sr-1,sc))

            if sr+1 < row and (sr+1,sc) not in visited and image[sr+1][sc] == st_color:
                image[sr+1][sc] = color 
                visited.add((sr+1,sc))
                q.append((sr+1,sc))

            if sc-1 >= 0 and (sr,sc-1) not in visited and image[sr][sc-1] == st_color :
                image[sr][sc-1] = color 
                visited.add((sr,sc-1))
                q.append((sr,sc-1))

            if sc+1 < col and (sr,sc+1) not in visited and image[sr][sc+1] == st_color:
                image[sr][sc+1] = color 
                visited.add((sr,sc+1))
                q.append((sr, sc+1))
        
        return image
