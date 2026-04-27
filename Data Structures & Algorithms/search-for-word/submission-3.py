class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # define directions 
        ROWS = len(board)
        COLS = len(board[0])


        # [[A,B],[C,D]]
        # AD
        def dfs(row, col, seen, target):
            # base case
            if target >= len(word):
                return True

            if (row, col) not in seen and row < ROWS and col < COLS and row >= 0 and col >= 0 and board[row][col] == word[target]:
                # print(row, col, board[row][col], seen)
                seen.add((row, col))

                arr = list(seen)

                # we need a new seen for each time we enter a dfs call
                return (
                    dfs(row + 1, col + 0, set(arr.copy()), target + 1) or 
                    dfs(row - 1, col + 0, set(arr.copy()), target + 1) or 
                    dfs(row + 0, col + 1, set(arr.copy()), target + 1) or 
                    dfs(row + 0, col - 1, set(arr.copy()), target + 1)
                )

            return False

        # loop through each item in the matrix and see if they match up
        for i in range(ROWS):
            for j in range(COLS):
                seen = set() # create a new set cache

                target = 0 # index of the word we are looking for

                # if at least one path matches, return True
                if dfs(i, j, seen, target):
                    return True

        return False

