class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        open_bracket = 0
        stack = []
        ans = ""

        for i in s:
            if i == "(":
                stack.append(i)
                open_bracket += 1
                if open_bracket > 1:
                    ans = ans + "("
            else:
                if open_bracket < 2:
                    stack.pop()
                    open_bracket -= 1
                else:
                    ans = ans + ")"
                    stack.pop()
                    open_bracket -= 1
        

        return ans