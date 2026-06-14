class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        Questions 
        1. board cannot be empty
        
        Thought process
        1. safe guard the O in the edges

        Analysis
        1. time | O(m) + O(n) + O(m*n)
        2. space | O(m * n)
        '''
        ROWS = len(board)
        COLS = len(board[0])
        safe = set()

        def dfs(row, col):
            # base case 
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or board[row][col] == "X" or (row, col) in safe:
                return

            safe.add((row, col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # O(n)
        for i in range(COLS):
            # row to be constant
            # first and last row
            if board[0][i] == "O":
                dfs(0, i)

            if board[ROWS - 1][i] == "O":
                dfs(ROWS - 1, i)

        # O(m)
        for j in range(ROWS):
            if board[j][0] == "O":
                dfs(j, 0)

            if board[j][COLS - 1] == "O":
                dfs(j, COLS - 1)

        # O(m * n)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O" and (i, j) not in safe:
                    board[i][j] = "X"