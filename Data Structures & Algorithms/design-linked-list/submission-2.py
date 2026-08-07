'''
Questions 
1. 

Thought process
1. Add at index:
    - loop until you get to specified index 
    - attach from the previous
2. Delete at index:
    - loop until index 
    - attach prev and next node of index
'''

class Node:
    def __init__(self, val = None, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:
    def __init__(self):
        # two sentinel nodes 
        self.head = Node(0)
        self.tail = Node(0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        curr = self.head.next

        while curr != self.tail and index:
            curr = curr.next
            index -= 1

        if curr == self.tail:
            return -1

        return curr.val


    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head, self.head.next)

        next__ = self.head.next

        self.head.next = node
        next__.prev = node

    def addAtTail(self, val: int) -> None:
        node = Node(val, self.tail.prev, self.tail)

        prev__ = self.tail.prev

        self.tail.prev = node
        prev__.next = node


    def addAtIndex(self, index: int, val: int) -> None:
        # count up till index 
        # attach from previous
        node = Node(val)

        curr = self.head.next

        while curr != self.tail and index:
            curr = curr.next
            index -= 1

        if curr == self.tail and not index:
            self.addAtTail(val)
            return

        if curr == self.tail and index:
            return 

        prev__ = curr.prev
        # point to node
        prev__.next = node
        curr.prev = node

        # node pointers
        node.next = curr
        node.prev = prev__

               
    def deleteAtIndex(self, index: int) -> None:
        curr = self.head.next 

        while curr != self.tail and index:
            curr = curr.next
            index -= 1

        # if index is invalid 
        if curr == self.tail:
            return 

        prev__ = curr.prev 

        curr.prev.next = curr.next
        curr.next.prev = curr.prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)