import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # All distinct solutions for N queen
        # generate board?? 
        # choice 
        # constraint 
        # goal
        res = []
        board = [(['.'] * n) for i in range(n)]
        COLS = set()
        POSDIAG = set()
        NEGDIAG = set()

        def backtrack(row):
            # base case 
            if row == n:
                clone = copy.deepcopy(board)
                res.append(["".join(clone[i]) for i in range(n)])
                return 

            for col in range(n):
                if col not in COLS and (row + col) not in POSDIAG and (row - col) not in NEGDIAG:
                    board[row][col] = "Q"
                    POSDIAG.add(row + col)
                    NEGDIAG.add(row - col)
                    COLS.add(col)

                    backtrack(row + 1)

                    board[row][col] = "."
                    POSDIAG.remove(row + col)
                    NEGDIAG.remove(row - col)
                    COLS.remove(col)
        
        backtrack(0)
        return res

        