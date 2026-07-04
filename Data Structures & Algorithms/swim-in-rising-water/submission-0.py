import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        '''
        Questions/clarifications
        1. grid is a square grid
        2. we cannot be given an empty grid
        3. if grid contains only one element. answer is the one element. return the one element
        4. will there always be a path to n - 1, n - 1
        5. are the items in the grid distinct

        Thought process/sub problems
        1. Minimum amount of time - djikstra
        2. return the count of visited nodes? 
            (steps, node)

        Time and Space complexity
        1. time | O((V + E) * log V)
        2. space | O(V + E)
        '''

        visited = set()
        ROWS = COLS = len(grid)
        res = 0

        # [[0]] - 0
        # [[0,1],[2,3]] - 3
        def dijkstra():
            heap = []

            heap.append((0, 0, 0)) # weight, rowIndex, colIndex

            while heap:
                nonlocal res 

                steps, row, col = heapq.heappop(heap)

                # if visited, skip
                # if (row, col) in visited: # do we need this?
                # continue
                # base case 
                # add to visited
                visited.add((row, col))

                # update res
                res = max(res, grid[row][col]) # keep track of the highest timestamp so far

                if row == ROWS - 1 and COLS - 1 == col:
                    return res

                # inspect neighbors
                for r, c in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nextRow = r + row
                    nextCol = c + col

                    if 0 <= nextRow < ROWS and 0 <= nextCol < COLS and (nextRow, nextCol) not in visited:
                        heapq.heappush(heap, (grid[nextRow][nextCol], nextRow, nextCol))

            return -1

        return dijkstra()