class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        '''
        Keywords
        1. Province = group of directly/indirectly connected cities
        2. Input is a matrix 

        Questions
        1. 

        Thought process
        1. 
        '''
        count = 0
        ROWS = len(isConnected)
        COLS = len(isConnected[0])
        visited = set()

        def dfs(node):
            # node becomes the row to inspect 
            for col in range(COLS):
                if isConnected[node][col] and (col) not in visited:
                    visited.add(col)
                    dfs(col)

        for row in range(ROWS):
            for col in range(COLS):
                if isConnected[row][col] and (col) not in visited:
                    visited.add(col)
                    dfs(col)
                    count += 1

        return count