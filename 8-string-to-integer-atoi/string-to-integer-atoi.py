class Solution:
    def myAtoi(self, s: str) -> int:
        # Initialize an empty list to store digits of the integer
        res = []
        # Initialize the sign to positive by default
        sign = 1
        # Boolean variable to track if we have started parsing the number
        started = False

        # Iterate through each character in the string
        for char in s:
            # Skip leading whitespace characters if parsing has started
            if char == ' ':
                if started:
                    break  # Stop parsing if we encounter whitespace after starting
                continue  # Skip leading whitespace
            
            # Handle the '+' sign
            if char == '+':
                # If parsing has started, stop parsing and return the result
                if started:
                    break  # Stop parsing if we encounter '+' after starting
                # Set parsing flag to True
                started = True
                continue
            # Handle the '-' sign
            elif char == '-':
                # If parsing has started, stop parsing and return the result
                if started:
                    break  # Stop parsing if we encounter '-' after starting
                # Set parsing flag to True
                started = True
                # Set the sign to negative
                sign = -1
                continue
            
            # If the character is a digit, add it to the result list and set the parsing flag to True
            if char.isdigit():
                res.append(char)
                started = True
            # If the character is not a digit, stop parsing
            else:
                break  # Stop parsing if we encounter non-numeric character after starting

        # If the result list is empty, return 0
        if not res:
            return 0

        # Convert the result list to an integer and apply the sign
        result = sign * int("".join(res))
        # Clamp the result to the range of a 32-bit signed integer
        if result < -2**31:
            return -2**31
        elif result > 2**31 - 1:
            return 2**31 - 1
        else:
            return result
