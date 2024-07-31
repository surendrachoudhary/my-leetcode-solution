class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        cache = {}
        def helper(i):
            if i == len(books):
                return 0 
            
            if i in cache:
                return cache[i]
            
            curr_weight = shelfWidth
            max_height = 0
            cache[i] = float("inf")
            for j in range(i, len(books) ):
                weight, height = books[j]

                if weight > curr_weight:
                    break 
                curr_weight -= weight  

                max_height = max(max_height, height)

                cache[i] = min (cache[i], 
                helper(j+1) + max_height)
            return cache[i] 

        return helper(0)



