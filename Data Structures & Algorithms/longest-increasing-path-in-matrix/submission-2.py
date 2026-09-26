class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        '''
        Keywords 
        1. matrix[i][j] >= 0
        2. no diagonal movement [manhattan distance]

        Thought Process 
        1. From constraints I'm thinking of dfs (word search, backtracking)
        2. memoization
        
        -------------------------
        DP
        - for each cell we want to know the max number of path 
        - memoization
        [
        [1,2],
        [2,1]
        ]
        top X 
        left X 
        right -> 
        - 
        '''
        ROWS = len(matrix)
        COLS = len(matrix[0])
        memo = {}
        DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row, col, memo):
            # if cell in memo, return max amount of count
            if (row, col) in memo:
                return memo[(row, col)]

            memo[(row, col)] = 1

            # base case 
            # if we can move no more, compare the length to global count
            for dr, dc in DIRECTIONS:
                next_row = dr + row 
                next_col = dc + col 

                if 0 <= next_row < ROWS and 0 <= next_col < COLS and matrix[row][col] < matrix[next_row][next_col]:
                    # add to visited 
                    memo[(row, col)] = max(memo[(row, col)], dfs(next_row, next_col, memo) + 1)

            return memo[(row, col)] 

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, memo)

        return max(memo.values())
