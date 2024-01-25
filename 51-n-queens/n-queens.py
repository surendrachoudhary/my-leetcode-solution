class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_set = set()
        posDig = set()
        negDig = set()
        res = []
        matrix = [["."] *n for i in range(n)]
        
        def backtrack(row):
            if row == n:
                # All rows filled, add this matrix to the result
                copy = ["".join(row) for row in matrix]
                res.append(copy)
                return

            for col in range(n):
                if col in col_set or (row-col) in negDig or (row+col) in posDig:
                    continue
                
                col_set.add(col)
                negDig.add(row-col)
                posDig.add(row+col)
                matrix[row][col] = 'Q'
                backtrack(row + 1)
                
                matrix[row][col] = '.'
                col_set.remove(col)
                negDig.remove(row-col)
                posDig.remove(row+col)

        
        backtrack(0)
        return res
