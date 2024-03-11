from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize an empty list to store the top k frequent elements
        ans = []
        # Count the frequency of each element in the input list
        counter = Counter(nums)
        # Initialize a heap to store tuples of frequency and element
        heap = []

        # Iterate through the items in the counter
        for num, freq in counter.items():
            # Push tuples containing frequency and element into the heap
            heapq.heappush(heap, (-freq, num))
        i = 1
        # Pop elements from the heap until it is empty
        while i <= k:
            # Pop the tuple with the highest frequency from the heap
            freq, num = heapq.heappop(heap)
            # Append the element to the answer list
            ans.append(num)

            i += 1

        # Return the top k frequent elements
        return ans
