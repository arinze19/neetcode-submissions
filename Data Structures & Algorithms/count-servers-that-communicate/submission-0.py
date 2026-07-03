class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        '''
        Questions 
        1. loop through each row and column
        2. keep a visited set to avoid readding added columns

        Thoguht process
        1. loop through each column in the first row 
        2. if find all "1" in the row and column and add to a set
        3. if set length is > 2, update count
        4. continue
        '''
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0

        def traverse(row, col):
            directions = [(1,0),(0,1),(-1,0),(0,-1)]

            for r, c in directions:
                dr = row + r
                dc = col + c

                while 0 <= dr < ROWS and 0 <= dc < COLS:
                    if grid[dr][dc] == 1:
                        return True
                    dr += r
                    dc += c

            return False

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and traverse(row, col):
                    count += 1

        return count