class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows = len(board)
        cols = len(board[0])

        for row in range(rows):
            for col in range(cols):
                # Define the directions: horizontal, vertical, and diagonal
                Directions = [(-1,-1), (-1,0), (-1, 1), (0, 1), (1,1), (1,0), (1,-1),(0,-1)]

                count = 0
                for dr, dc in Directions:
                    new_row, new_col = row + dr, col + dc

                    if 0 <= new_row < rows and 0<= new_col < cols:
                        neighbour = board[new_row][new_col]
                        if neighbour == 1 or neighbour == "*":
                            count += 1
                    
                if count < 2 and (board[row][col] == 1 or board[row][col] == "*"):
                    board[row][col] = "*"
                elif (board[row][col] == 1 or board[row][col] == "*") and count > 3:
                    board[row][col] = "*"
                elif( board[row][col] == 0 or board[row][col] == ".") and count == 3:
                    board[row][col] = "."

        #changing the value after the complete traversal              
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "*":
                    board[i][j] = 0
                elif board[i][j] == ".":
                    board[i][j] = 1
                




        """
        Do not return anything, modify board in-place instead.
        """
        