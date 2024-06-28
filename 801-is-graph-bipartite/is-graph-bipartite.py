class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color_list = [0] * (n)
        visited_set = set()
        
        def bfs(i):
            q = deque()
            q.append(i)
            visited_set.add(i)

            color_list[i] = -1

            while q:
                node = q.popleft()

                for nei in graph[node]:
                    if nei not in visited_set:
                        color_list[nei] = -color_list[node] 
                        q.append(nei)
                        visited_set.add(nei)
                    elif color_list[nei] == color_list[node]:
                        return False 
            return True 

        for i in range(n):
            if i not in visited_set:
                if not bfs(i):
                    return False 
       
        # print(color_list)        
        return True 

     
