class Solution:
    def climbStairs(self, n: int) -> int:
        dp_array = [0] * (n + 1 )
        if n == 1:
            return 1
        dp_array[1] = 1 
        dp_array[2] = 2 

        num = 3
        while num <= n:
            dp_array[num] = dp_array[num-1] + dp_array[num-2]
            num += 1

        return dp_array[n]