class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        ans = ""

        for char in s:
            if char == "(":
                if stack:  # If stack is not empty, add the current character to ans
                    ans += char
                stack.append(char)
            else:
                stack.pop()  # Remove the corresponding "(" from stack
                if stack:  # If stack is not empty, add the current character to ans
                    ans += char
        
        return ans
