class Solution:
    def fib(self, n: int) -> int: 
        if n < 2:
            return n


        result = self.fib(n-1) + self.fib(n-2)
        return result 