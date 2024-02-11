class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize an empty list to store the resulting triangle
        res = []

        # Iterate over each row in the triangle
        for i in range(numRows):
            # Calculate the number of elements in the current row
            n = i + 1
            
            # Initialize a list to store the current row with the first element as 1
            cur_res = [1]
            
            # Initialize ans to 1
            ans = 1
            
            # Iterate through the row to calculate each element
            for j in range(1, n):
                # Update ans using the formula for binomial coefficients (n choose j)
                ans *= (n - j)
                ans //= j
                
                # Append the calculated value to the current row
                cur_res.append(ans)
            
            # Append the current row to the result triangle
            res.append(cur_res)

        # Return the resulting Pascal's Triangle
        return res
