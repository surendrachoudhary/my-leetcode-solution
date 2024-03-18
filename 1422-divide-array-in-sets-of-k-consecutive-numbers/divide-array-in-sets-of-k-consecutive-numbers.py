class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        from collections import Counter
        # Check if the total number of cards is divisible by groupSize
        if len(nums) % k != 0:
            return False
        
        # Count occurrences of each card value
        counts = Counter(nums)
        print(counts)
        print(sorted(counts.keys()))
        
        # Process the counts sequentially
        for card in sorted(counts.keys()):
            count = counts[card]
            if count > 0:
                # Check if counts of consecutive group of cards are present
                for i in range(k):
                    if counts[card + i] < count:
                        return False
                    counts[card + i] -= count
                    
        # If all conditions pass, return True
        return True
