class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        Questions 
        1. Find all cells where the water can flow to both oceans

        Thought process
        1. Tag all cells that lead to atlantic ocean 
        2. Starting from all cells in pacific ocean, try to connect and see if we can get to at least one cell in atlantic
            - if so, add the route to a set
        '''
        # reversing the question
        # for the sets we want to see how far we can connect upstream
        ROWS = len(heights)
        COLS = len(heights[0])
        res = []

        if not ROWS or not COLS:
            return res

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # pacific and atlantic items
        pacific = set()
        atlantic = set()

        def is_valid(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS

        def dfs(row, col, visited, prevHeight):
            # add to visited 
            visited.add((row, col))

            # go through neighbors
            for x, y in directions:
                next_row = x + row
                next_col = y + col

                if (next_row, next_col) not in visited and \
                 is_valid(next_row, next_col) and \
                 heights[row][col] <= heights[next_row][next_col]:
                    dfs(next_row, next_col, visited, heights[row][col])

        for r in range(ROWS):
            # for first col (pacific)
            if (r, 0) not in pacific:
                dfs(r, 0, pacific, heights[r][0])

            # for last col (atlantic)
            if (r, COLS - 1) not in atlantic:
                dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        for c in range(COLS):
            # for first row (pacific)
            if (0, c) not in pacific:
                dfs(0, c, pacific, heights[0][c])

            # for last row (atlantic)
            if (ROWS - 1, c) not in atlantic:
                dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        # identify cells that appear in both sets
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res