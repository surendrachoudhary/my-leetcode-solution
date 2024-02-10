class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Initialize an empty list to store the resulting row
        res = []

        # Define a helper function to calculate the value of nCr
        def nCr(r, c):
            # Initialize the value to 1
            value = 1

            # Calculate the value of nCr using the formula (r choose c)
            for i in range(c):
                value *= r-i
                value //= i+1

            # Return the calculated value
            return value
        
        # Iterate over each index in the row up to the specified rowIndex
        for i in range(rowIndex+1):
            # Append the value of nCr to the result list
            res.append(nCr(rowIndex, i))

        # Return the resulting row
        return res
