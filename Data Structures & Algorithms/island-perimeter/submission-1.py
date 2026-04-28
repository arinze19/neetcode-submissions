class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # INPUT AND OUTPUT
        # 1 represents land 
        # 0 represents water 
        # grid is surrounded by water 
        # land does not have lakes 
        # one square has a length 1
        # return permimeter

        # THOUGHT PROCESS 
        # go through each cell and pick out the connecting neighbors 
        # have a global seen variable 
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()
        res = 0

        def dfs(row, col):
            # base case 
            if (row, col) in seen: 
                return 0
            
            if row >= ROWS or col >= COLS or col < 0 or row < 0 or grid[row][col] == 0:
                return 1
            
            # recursive case 
            # if row < ROWS and col < COLS and col >= 0 and row >= 0 and grid[row][col] == 1 and (row, col) not in seen:
            seen.add((row, col))
            return dfs(row + 1, col + 0) + dfs(row - 1, col + 0) + dfs(row + 0, col + 1) + dfs(row, col - 1)
            # add it to a global result
            # return 1



        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    return dfs(i, j)

        return 0

