import heapq
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Check if the total number of cards is divisible by groupSize
        if len(hand) % groupSize:
            return False

        # Initialize a dictionary to count the occurrences of each card
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        # Convert the keys of the count dictionary to a list and heapify it
        minH = list(count.keys())
        heapq.heapify(minH)

        # Process the cards sequentially
        while minH:
            # Get the smallest card from the min heap
            first = minH[0]
            # Check if consecutive cards of groupSize are present
            for i in range(first, first + groupSize):
                if i not in count:  # If the card is missing from the count
                    return False
                count[i] -= 1  # Decrease the count of the card
                if count[i] == 0:  # If the count becomes zero, remove it
                    if i != minH[0]:  # If it's not the current smallest card
                        return False
                    heapq.heappop(minH)  # Remove the card from the heap
        return True
