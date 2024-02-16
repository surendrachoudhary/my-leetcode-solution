from collections import Counter

class Solution:
    def majorityElement(self,arr):
        # Size of the given array
        n = len(arr)

        # Count the occurrences of each element using Counter
        counter = Counter(arr)

        # Searching for the majority element
        for num, count in counter.items():
            if count > (n // 2):
                return num

        return -1