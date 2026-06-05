class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        Questions
        1. If we have no islands available, return 
        2. Can we update the input argument??

        Thought Process
        1. each time we come across a "1" we want to get the total number of "1" attached 
        2. for each "1" we come across we want to add it to the seen set? or convert it into a "0"
        3. compare total number of "1" attached to current res when we hit a base case

        Sub-problems 
        1. traverse thorugh the grid
        2. identify base case 
        3. keep count of max of current island
        4. update result 
        '''
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])


        def dfs(row, col):
            # base case 
            if row >= ROWS or col >= COLS or col < 0 or row < 0 or not grid[row][col]:
                return 0

            grid[row][col] = 0
            return 1 + (dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    count = dfs(i, j)
                    res = max(res, count)

        return res
