"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        Questions
        1. node can be empty?? Yes 
        2. duplicate nodes?? No

        Thought Process
        0. if not node: return node
        1. dfs(node)
            cloneNode = Node(node.val)
            - for child in node.neighbors
            - if child not in seen
            - newNode = dfs(child)
            - node.children.append(newNode)
            - newNode.children.append(node)



            [[]] [done]
            [[2],[1,3],[2]] | seen = set()
                - cloneNode (1) | seen = <0x(1)>
                    - dfs(2)
                    - cloneNode (2) | seen = <0x(1), 0x(2)>
                        - dfs(3)
                        - cloneNode (3) | seen = <0x(1), 0x(2), 0x(3)>
                            - dfs(3)

                        * newNode(3)
                        - newNode.children.append(cloneNode)
                        - cloneNode.children.append(newNode)
                    
                    * newNode(2)
                    - newNode.children.append(cloneNode)
                    - cloneNode.children.append(newNode)
        '''
        if not node:
            return None

        seen = {}

        def dfs(root):
            if root in seen: 
                return seen[root]
                
            if root not in seen:
                seen[root] = Node(root.val)

            for child in root.neighbors:
                seen[root].neighbors.append(dfs(child))
            
            return seen[root]

        return dfs(node)
        