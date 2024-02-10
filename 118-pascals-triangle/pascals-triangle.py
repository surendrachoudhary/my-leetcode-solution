#O(n^2) time complexity 

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the result list with the first row containing a single element 1
        res = [[1]]

        # Loop through to generate subsequent rows up to the given numRows
        for i in range(numRows-1):
            # Create a temporary row with padding of 0s on both sides
            temp = [0] + res[-1] + [0]
            row = []

            # Calculate values for the current row based on the previous row
            for j in range(len(res[-1])+1):
                row.append(temp[j] + temp[j+1])

            # Append the generated row to the result list
            res.append(row)
        
        # Return the resulting Pascal's Triangle up to the specified number of rows
        return res
