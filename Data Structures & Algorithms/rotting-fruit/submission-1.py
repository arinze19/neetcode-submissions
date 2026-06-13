from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # min number of minutes to elapse before no fresh fruit in grid
        '''
        Question
        1. 10X10 matrix at maximum
        2. grid cannot be empty
        3. if solution not possible return -1
        4. how many rotten fruits can we expect? More than one

        Thought process
        1. bfs from starting rotten fruit
        2. if empty cell return
        3. how to calculate time? number of levels
        4. multi source bfs??
        '''
        queue = deque([])
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        count = 0

        # runtime | O(m * n)
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i, j))


        # runtime | O(m + n)
        # space | O(m + n)
        while queue:
            n = len(queue)
            for i in range(n):
                row, col = queue.popleft()
                for dr, dc in directions:
                    r = dr + row
                    c = dc + col
                    if r >= 0 and c >= 0 and r < ROWS and c < COLS and grid[r][c] == 1:
                        grid[r][c] = 2
                        queue.append((r,c))

            if queue:
                count += 1
            # increment at the end of the queue

        # runtime | O(m * n)
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1

        return count
