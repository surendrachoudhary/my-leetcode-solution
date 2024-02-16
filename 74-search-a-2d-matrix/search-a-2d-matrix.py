class Solution:
    def searchMatrix(self, matrix, target):
        # Get the number of rows and columns in the matrix
        n = len(matrix)
        m = len(matrix[0])

        # Apply binary search on the flattened matrix
        low = 0
        high = n * m - 1
        while low <= high:
            mid = (low + high) // 2
            # Convert the flattened index back to row and column numbers
            row = mid // m 
            col = mid % m
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
