from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        '''
        Are we guaranteed that image[sr][sc] will not be color?? No
        can we have an empty image?? No
        [[0,1],[1,1]] | sr = 1, sc = 1, color = 0

        Thought process
        bfs

        Time and Space
        time = O(m * n)
        space = O(1)
        '''
        queue = deque([(sr, sc)])
        target = image[sr][sc]
        ROWS = len(image)
        COLS = len(image[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # if starting cell already of type color
        if target == color:
            return image

        while queue:
            i, j = queue.popleft()

            image[i][j] = color

            for row, col in directions:
                nextRow = row + i
                nextCol = col + j

                if nextRow >= 0 and nextCol >= 0 and nextRow < ROWS and nextCol < COLS and image[nextRow][nextCol] == target:
                    queue.append((nextRow, nextCol))
                    
        return image
