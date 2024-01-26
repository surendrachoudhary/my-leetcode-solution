class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def solver(board):
            for i in range(rows):
                for j in range(cols):
                    if board[i][j] == ".":
                        for c in "123456789":
                            if isValid(board, i, j , c):
                                board[i][j] = c

                                if (solver(board)):
                                    return True 
                                else:
                                    board[i][j] = "."
                        return False 
            return True 

        def isValid(board, row, col, c):
            for i in range(9):
                if board[row][i] == c:
                    return False

                if board[i][col] == c:
                    return False     

                if board[3*(row//3) + i//3][3*(col//3) + i%3] == c:
                    return False
            return True    

        solver(board)


        """
        Do not return anything, modify board in-place instead.
        """
        