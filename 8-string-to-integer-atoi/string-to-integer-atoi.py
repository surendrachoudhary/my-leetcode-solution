class Solution:
    def myAtoi(self, s: str) -> int:
        res = []
        sign = 1  # Default positive sign
        started = False  # To track if we have started parsing the number

        for char in s:
            if char == ' ':
                if started:
                    break  # Stop parsing if we encounter whitespace after starting
                continue  # Skip leading whitespace
            
            if char == '+':
                if started:
                    break  # Stop parsing if we encounter '+' after starting
                started = True
                continue
            elif char == '-':
                if started:
                    break  # Stop parsing if we encounter '-' after starting
                started = True
                sign = -1
                continue
            
            if char.isdigit():
                res.append(char)
                started = True
            else:
                break  # Stop parsing if we encounter non-numeric character after starting

        if not res:  # Check if res is empty
            return 0

        result = sign * int("".join(res))
        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1
        else:
            return result
