class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Initialize an empty list to store the resulting row
        res = [1]

        # Calculate the number of elements in the row
        n = rowIndex + 1
        
        # Initialize ans to 1
        ans = 1
        
        # Iterate through the row to calculate each element
        for i in range(1, n):
            # Update ans using the formula for binomial coefficients (n choose i)
            ans *= (n - i)
            ans //= i
            
            # Append the calculated value to the result list
            res.append(ans)

        # Return the resulting row
        return res
