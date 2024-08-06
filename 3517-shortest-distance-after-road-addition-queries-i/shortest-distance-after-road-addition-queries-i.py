class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj_list = [[] for i in range(n)]
        
        for i in range(n-1):
            adj_list[i].append((i+1, 1))

        def dijskrta():
            distance = [float("inf")] * n
            distance[0] = 0

            pq = [(0,0) ]#(weight, node)
            while pq:
                weight,node = heapq.heappop(pq)

                for nxt_node, nxt_weight in adj_list[node]:
                    total_weight = weight + nxt_weight
                    if total_weight < distance[nxt_node]:
                        distance[nxt_node] = total_weight
                        heapq.heappush(pq, (total_weight, nxt_node))
            return distance[n-1]

        result = []
        for u, v in queries:
            adj_list[u].append((v, 1))
            result.append(dijskrta())

        return result


        