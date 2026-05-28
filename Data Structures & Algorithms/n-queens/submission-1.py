class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = [] # result
        board = [['.' for i in range(n)] for j in range(n)] # generate the board dimensions

        def isSafe(row, col, board):
            # inspect the cols and diagonals above the current pos
            # since lower positions will not be filled yet because we traverse top to bottom
            left = right = col

            while row >= 0: 
                if (
                    left >= 0 and board[row][left] == "Q" or
                    right < len(board) and board[row][right] == "Q" or 
                    board[row][col] == "Q"
                    ):
                    return False
                else:
                    left -= 1
                    right += 1
                    row -= 1

            return True

        def backtrack(row, board):
            # base case 
            if row == n:
                # convert the matrix into a string to match with the expected output
                res.append(["".join(boardRow) for boardRow in board])
                return

            # recursive case
            for col in range(n):
                if isSafe(row, col, board):
                    board[row][col] = "Q"
                    # for each correct placement at the row level we want to 
                    # extend down until the final row and take a snapshot of our state
                    backtrack(row + 1, board) 
                    board[row][col] = "."

        backtrack(0, board)

        return res
