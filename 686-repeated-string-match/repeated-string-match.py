class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        min_repeat = -(-len(b)//len(a))

        string = a * min_repeat

        
        if b in string:
            return min_repeat
        
        string += a

        if b in string:
            return min_repeat + 1

        return -1

        
