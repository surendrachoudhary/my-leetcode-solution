class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Initialize the indices for the bottom-left corner of the matrix
        row, col = len(matrix) - 1, len(matrix[0]) - 1
        cur_row, cur_col = 0, col 
        
        # Iterate until the current row and column indices are within the matrix bounds
        while cur_row <= row and cur_col >= 0:
            # If the current element equals the target, return True
            if matrix[cur_row][cur_col] == target:
                return True 
            # If the current element is greater than the target, move leftwards in the same row
            elif matrix[cur_row][cur_col] > target:
                cur_col -= 1
            # If the current element is less than the target, move downwards in the same column
            else:
                cur_row += 1
        
        # If the target is not found, return False
        return False 
