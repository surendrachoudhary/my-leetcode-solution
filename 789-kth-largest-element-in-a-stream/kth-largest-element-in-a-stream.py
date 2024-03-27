import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        # Adjust the heap so that it contains at most k elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        # If adding val exceeds k, pop the smallest element to maintain k largest elements
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # Return the kth largest element
        return self.heap[0]

# Example usage:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
