class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color_list = [0] * n  # 0: uncolored, 1: color1, -1: color2

        def dfs(i):
            for nei in graph[i]:
                if color_list[nei] == 0:
                    color_list[nei] = - color_list[i]
                    if not dfs(nei):
                        return False 
                elif color_list[nei] == color_list[i]:
                    return False 
            
            return True 


        for i in range(n):
            if color_list[i] == 0:
                color_list[i] = 1
                if not dfs(i):
                    return False

        print(color_list)
        return True


