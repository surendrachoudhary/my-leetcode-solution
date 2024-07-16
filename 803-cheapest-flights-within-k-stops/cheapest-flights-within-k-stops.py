class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = [[] for _ in range(n)]

        for fro, to, price in flights:
            adj_list[fro].append((to,price))

        output = [(float("inf"), float("inf"))] * n
        pq = [(0, 0, src)]

        output[src] = (0,0)
        while pq:
            cost, step, node = heapq.heappop(pq)

            if node == dst:
                return cost

            if step > k:
                continue 

            for dis, costing in adj_list[node]:
                total_costing = cost + costing
                output_cost, output_step = output[dis] 
                if total_costing < output_cost or step < output_step:
                    output[dis] = (total_costing, step)
                    heapq.heappush(pq, (total_costing, step+1, dis))
        
        return -1 if output[dst][0] == float("inf") else output[dst][0]
        