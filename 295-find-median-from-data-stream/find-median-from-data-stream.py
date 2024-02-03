import heapq

class MedianFinder:
    def __init__(self):
        # Initialize two heaps: self.small for the max heap (representing the first half of numbers)
        # and self.large for the min heap (representing the second half of numbers).
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # Add the negation of the number to create a max heap in Python.
        heapq.heappush(self.small, -1 * num)

        # Maintain balance between the two heaps.
        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Ensure the size difference between heaps does not exceed 1.
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # Return the top of the max heap if its size is greater.
        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        # Return the top of the min heap if its size is greater.
        if len(self.large) > len(self.small):
            return self.large[0]

        # Calculate and return the median if both heaps are of equal size.
        return (-1 * self.small[0] + self.large[0]) / 2
