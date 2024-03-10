class Solution:
    def reverse(self, x: int) -> int:
        s = ""
        sign = 1

        for i in str(x):
            if i == "-":
                sign = -1
            else:
                s = i + s

        result = sign * int(s)

        if result < -2**31:
            return 0
        elif result > 2**31-1:
            return 0
        else:
            return result 
