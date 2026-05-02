# tree data structure 
# children
# ListNode:
#   value: string
#   children: [ListNode]
#   is_end: bool
class TrieNode:
    def __init__(self, children = None, is_end = False):
        if children:
            self.children = children
        else:
            self.children = {}

        self.is_end = is_end


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
       # initiate at root node
        node = self.root

        # loop through char
        for char in word:
            if char in node.children: # if char present in node children, move to char TrieNode
                node = node.children[char]
            else:
                # else create new child node from char and move into newly created child node
                new_node = TrieNode()
                node.children[char] = new_node
                node = new_node
        
        node.is_end = True # after insert, toggle `is_end`


    def search(self, word: str) -> bool:
        # initiate at root node
        node = self.root

        # loop through char
        for char in word:
            if char not in node.children: # if current char not in current node children, return False
                return False 
            else:
                node = node.children[char] # else move into next char TrieNode

        return node.is_end # return is_end status of last TrieNode
        
    def startsWith(self, prefix: str) -> bool:
        # initiate at root node
        node = self.root

        # loop through char
        for char in prefix:
            if char not in node.children: # if char not in current node children, there is no prefix, return False
                return False
            else:
                node = node.children[char] # move into next char TrieNode
        
        return True # if we complete the loops, return True

        
        