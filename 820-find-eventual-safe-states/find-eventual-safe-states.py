# BFS technique (DFS is better than BFS but you should know this as we are here to build logic and not to slove question)

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        rev_adj = [[] for _ in range(n)]
        indegrees = [0] * n

        for node, neighbours in enumerate(graph):
            for neighbour in neighbours:
                rev_adj[neighbour].append(node)
                indegrees[node] += 1
        
        q = deque()

        for i in range(n):
            if indegrees[i] == 0:
                q.append(i)

        safe = [False] * n
        while q:
            node = q.popleft()
            safe[node] = True

            for nei in rev_adj[node]:
                indegrees[nei] -= 1

                if indegrees[nei] == 0:
                    q.append(nei)

        safe_nodes = []

        for i in range(n):
            if safe[i]:
                safe_nodes.append(i)
            
        return safe_nodes
            

        