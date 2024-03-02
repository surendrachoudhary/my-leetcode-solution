class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row,col = 0,len(matrix[0])-1


        while row < len(matrix):
            low, high = 0,col    
            while low <= high:

                mid = (low+high)//2

                if matrix[row][mid] == target:
                    return True

                elif matrix[row][mid] > target:
                    high = mid -1

                else:
                    low = mid + 1
            row += 1

        return False 