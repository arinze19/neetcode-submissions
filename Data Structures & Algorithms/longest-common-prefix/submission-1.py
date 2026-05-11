class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = 0
        root = TrieNode()
        node = root
        
        # O(m)
        for word in strs:
            # O(n)
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.isEndOfWord = True

            node = root

        def dfs(node, count): # O(min(strs))
            nonlocal res

            # base case
            if len(node.children) != 1 or node.isEndOfWord:
                res = max(res, count)
                return

            count += 1

            res = max(res, count)

            for child in node.children:
                dfs(node.children[child], count)


        dfs(root, 0)

        return strs[0][:res]