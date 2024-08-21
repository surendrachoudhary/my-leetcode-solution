class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        def helper(count, paste):
            if count == n:
                return 0
            if count > n:
                return 1000
            
            #Paste 
            res1 = 1 + helper(count + paste, paste)

            # copy and paste 
            res2 = 2 + helper(count + count, count)

            return min(res1, res2)
            
        return 1 + helper(1, 1)