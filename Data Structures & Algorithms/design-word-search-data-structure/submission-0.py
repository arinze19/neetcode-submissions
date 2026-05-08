class TrieNode:
    def __init__(self, children = None, isEndOfWord = False):
        if not children:
            self.children = {}
        else:
            self.children = children

        self.isEndOfWord = isEndOfWord

class WordDictionary:

    def __init__(self):   
        self.root = TrieNode()

    def addWord(self, word: str) -> None: #O(n)
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        node = self.root
        res = False

        def dfs(j, root):
            node = root

            for i in range(j, len(word)):
                char = word[i]

                if char == ".":
                    for child in node.children:
                        if dfs(i + 1, node.children[child]):
                            return True
                    return False
                else:
                    if char not in node.children:
                        return False
                    node = node.children[char]
            return node.isEndOfWord
            

        return dfs(0, self.root)

        # "abc" 
        # - "ab" [done]
        # - "abc" [done]
        # - ".bc"
        


        
