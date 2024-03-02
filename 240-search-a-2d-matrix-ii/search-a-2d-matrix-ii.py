class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Initialize the starting row and column indices
        row, col = 0, len(matrix[0]) - 1

        # Iterate through the matrix rows
        while row < len(matrix):
            # Initialize the binary search boundaries for the current row
            low, high = 0, col

            # Perform binary search within the current row
            while low <= high:
                mid = (low + high) // 2

                # If the target is found, return True
                if matrix[row][mid] == target:
                    return True
                # If the target is less than the current element, update the high boundary
                elif matrix[row][mid] > target:
                    high = mid - 1
                # If the target is greater than the current element, update the low boundary
                else:
                    low = mid + 1
            
            # Move to the next row
            row += 1

        # If the target is not found in any row, return False
        return False
