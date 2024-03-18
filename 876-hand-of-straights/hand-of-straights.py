from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Check if the total number of cards is divisible by groupSize
        if len(hand) % groupSize != 0:
            return False
        
        # Count occurrences of each card value
        counts = Counter(hand)
        
        # Process the counts sequentially
        for card in sorted(counts.keys()):
            count = counts[card]
            if count > 0:
                # Check if counts of consecutive group of cards are present
                for i in range(groupSize):
                    if counts[card + i] < count:
                        return False
                    counts[card + i] -= count
                    
        # If all conditions pass, return True
        return True
