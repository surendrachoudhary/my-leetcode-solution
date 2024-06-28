class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color_list = [0] * n  # 0: uncolored, 1: color1, -1: color2

        def bfs(start):
            q = deque([start])
            color_list[start] = 1  # Start coloring with 1

            while q:
                node = q.popleft()
                for neighbor in graph[node]:
                    if color_list[neighbor] == 0:  # If not colored, color with opposite color
                        color_list[neighbor] = -color_list[node]
                        q.append(neighbor)
                    elif color_list[neighbor] == color_list[node]:  # If same color as current node, not bipartite
                        return False
            return True

        # Need to check each component of the graph
        for i in range(n):
            if color_list[i] == 0:  # If the node is not yet colored, start a BFS
                if not bfs(i):
                    return False

        return True
