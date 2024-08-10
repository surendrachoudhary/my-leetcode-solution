class Solution:
    def climbStairs(self, n: int) -> int:
        dic = {}
        def helper(n):
            if n == 0:
                return 1

            if n < 0:
                return 0

            if n in dic:
                return dic[n]

            dic[n] = helper(n-1) + helper(n-2)
            return dic[n]
        return helper(n)