"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        INSIGHT
        1. create a deep copy of list
        
        INPUT AND OUTPUT
        1. we could have empty head
        
        THOUGHT PROCESS
        0. if not head: return head
        1. add the head into an array
        2. creating a dummy node so I have a new list
        3. loop through array and place items
            - account for if not index
            - account for random pointing to self*
        4. return dummy.next

        QUESTIONS:
        1. are the values unique? 
        2. 
        """
        if not head: 
            return head

        arr = []
        arr2 = []
        cache = {}

        curr = head

        while curr:
            arr.append(curr)
            curr = curr.next

        for i in range(len(arr)):
            cache[arr[i]] = i

        dummy = Node(0)

        for i in range(len(arr)):
            # create a new node
            # point the node.next to cache[arr[i]].next
            next__ = cache.get(arr[i].next, None)
            random = cache.get(arr[i].random, None)
            value = arr[i].val

            arr2.append([value, next__, random])
        
        for i in range(len(arr)):
            arr[i] = Node(arr[i].val)

        for i in range(len(arr)):
            next__ = arr2[i][1]
            random = arr2[i][2]

            if next__ != None:
                arr[i].next = arr[next__]
            else:
                arr[i].next = None

            if random != None:
                arr[i].random = arr[random]
            else:
                arr[i].random = None

        return arr[0]

        
        