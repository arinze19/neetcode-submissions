def minimumEffortPath(heights):
        '''
        Questions
        1. empty list? No
        2. possible to have one input? return input
        3. return the max and min between paths

        Thought process
        1. dfs through the matrix
        2. append the path to an array 
        3. base case when row = ROW - 1 and col = COL - 1
            - get min and max of paths so far
            - compare against global min
        4. return global min
        '''
        ROWS = len(heights)
        COLS = len(heights[0])
        visited = set([(0, 0)])
        res = float("inf")
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(row, col, path):
            # init non-local 
            nonlocal res
            
            # base case (end case)
            if row == ROWS - 1 and col == COLS - 1:
                mini = min(path)
                maxi = max(path)

                res = min(res, abs(mini - maxi))
                return

            # inspect neighbors
            for r, c in directions:
                dr = r + row
                dc = c + col
                
                if dr < 0 or dc < 0 or dr >= ROWS or dc >= COLS or (dr, dc) in visited:
                    continue 
                
                path.append(heights[dr][dc])
                visited.add((dr, dc))
                
                dfs(dr, dc, path)
                
                path.pop()
                visited.remove((dr, dc))

        dfs(0, 0, [heights[0][0]])

        return 0
    
# minimumEffortPath([
#     [1,2,2],
#     [3,8,2],
#     [5,3,5]
# ])

