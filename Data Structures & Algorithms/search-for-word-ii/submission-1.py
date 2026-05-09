class TrieNode: 
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # initiate variables
        ROWS = len(board)
        COLS = len(board[0])

        res = []

        # initiate a trie node root
        root = TrieNode()

        # create Prefix Tree
        for word in words:
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]

            node.isEndOfWord = True

        def dfs(i, j, node, word, seen):
            nonlocal res
            # 0 0 Node(a) [a] (0,0)
            # 0 1 Node(b) [a,b] [(0,0),(0,1)]
            if node.isEndOfWord:
                res.append("".join(word))
                node.isEndOfWord = False

            # recursive case 
            directions = [(1,0),(-1,0),(0,1),(0,-1)]

            for dr, dc in directions:
                row = dr + i
                col = dc + j

                if row >= 0 and \
                   col >= 0 and \
                   (row, col) not in seen and \
                   col < COLS and \
                   row < ROWS and \
                   board[row][col] in node.children:
                    seen.add((row, col))
                    word.append(board[row][col])

                    dfs(row, col, node.children[board[row][col]], word, seen)

                    seen.remove((row, col)) # verify if this most optimal way to pop
                    word.pop()

        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] in root.children:
                    seen = set()
                    seen.add((i, j))
                    dfs(i, j, root.children[board[i][j]], [board[i][j]], seen)

        return res

