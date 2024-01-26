class Solution:
    def totalNQueens(self, n: int) -> int:
        col_set = set()
        posDig = set()
        negDig = set()
        # res = [0]  # Using a list to hold the result

        matrix = [["."] * n for i in range(n)]

        def backtrack(row):
            if row == n:
                # All rows filled, add this matrix to the result
                # res[0] += 1
                return 1
            cnt = 0
            for col in range(n):
                if col in col_set or (row - col) in negDig or (row + col) in posDig:
                    continue

                col_set.add(col)
                negDig.add(row - col)
                posDig.add(row + col)
                matrix[row][col] = 'Q'
                cnt += backtrack(row + 1)

                matrix[row][col] = '.'
                col_set.remove(col)
                negDig.remove(row - col)
                posDig.remove(row + col)
            
            return cnt 

        return backtrack(0)
        # return res[0]
