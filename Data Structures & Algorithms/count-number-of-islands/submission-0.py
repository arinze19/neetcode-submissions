class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Questions 
        1. can we have an empty grid?? No
        2. if no islands found we return 0?? Yes

        Thought process
        1. we can loop through the grid 
            - at each occurence of 1, we "capture" the adjacent "1" next to it and add the (row, col) to a seen set
            - add one to our count
        2. for subsequent occurence we see if we have that (row, col) in our seen set
        '''
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()

        def dfs(row, col):
            # base case 
            if row >= ROWS or col >= COLS or (row, col) in seen or row < 0 or col < 0 or grid[row][col] == "0":
                return


            # dfs in four directions
            seen.add((row, col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i,j) not in seen:
                    dfs(i, j)
                    res += 1

        return res
