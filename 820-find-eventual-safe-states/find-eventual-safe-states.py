class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        total_nodes = len(graph)
        visited_set = [False] * total_nodes
        recursion_set = [False] * total_nodes
        safe_node = [False] * total_nodes

        def dfs(node):
            visited_set[node] = True 
            recursion_set[node] = True 

            for nei in graph[node]:
                if not visited_set[nei]:
                    if dfs(nei):
                        return True 
                         
                elif recursion_set[nei]:
                    return True  
            
            
            safe_node[node] = True 

            recursion_set[node] = False 

           

        for node in range(total_nodes):
            if not visited_set[node]:
                dfs(node)

        result = [ node for node in range(len(safe_node)) if safe_node[node] ]
        return result 