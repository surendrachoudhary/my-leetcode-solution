#time complexity - O(n^3)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize an empty list to store the resulting triangle
        res = []

        # Define a helper function to calculate nCr
        def nCr(r, c):
            value = 1

            # Calculate nCr using the formula (r choose c)
            for i in range(c):
                value *= r-i
                value //= i+1

            return value

        # Iterate over each row in the triangle
        for i in range(numRows):
            # Initialize an empty list to store the current row
            cur_res = []

            # Iterate over each column in the current row
            for j in range(i+1):
                # Append the value of nCr to the current row
                cur_res.append(nCr(i, j))
            
            # Append the current row to the result triangle
            res.append(cur_res)

        # Return the resulting Pascal's Triangle
        return res
