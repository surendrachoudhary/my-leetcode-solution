class Solution:
    def reverse(self, x: int) -> int:
        # Extracting the sign of the input integer
        sign = 1 if x >= 0 else -1
        # Converting negative numbers to positive for reversal
        x = abs(x)
        
        result = 0
        
        while x:
            result = (result * 10) + x % 10 
            x = x // 10

        # Applying the sign to the result
        result *= sign

        # Check if the result overflows 32-bit integer range
        if result < -2**31 or result > 2**31 - 1:
            return 0
        else:
            return result
