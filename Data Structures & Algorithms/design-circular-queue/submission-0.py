class Node:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev 
        self.next = next 

class MyCircularQueue:
    '''
    Keywords
    1. last ring connected to first ring
    2. "In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue"
        - 

    Questions.
    1. We want the operations of this queue to match the runtime of a normal queue as much as possible (O(1) pop and append)
    2. Does the part of it being circular affect the design? 

    Thought Process
    1. doubly linked list
    2. two sentinel nodes 
    3. Front. gets items from the front
    4. Rear. gets items from the tail
    5. enQueue? adds an elemtn into the circular queue (front or back)
    6. isEmpty: this.head.next == this.tail
        - we can also keep track of the count of items in the queue by using a global count
    7. count the nodes in the list. if count == n. return True else return False O(n)
        - we can optimize by keeping track of the items count in the queue (O(1))

    Runtime 
    time | O(1) for all operations 
    space | O(n) 
    '''

    def __init__(self, k: int):
        self.head = Node(0)
        self.tail = Node(0)
        self.count = 0
        self.capacity = k

        # update next and prev 
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def enQueue(self, value: int) -> bool:
        # early return
        if self.count >= self.capacity:
            return False 

        # add to the back
        node = Node(value)

        prev__ = self.tail.prev 

        # update queue pointers
        self.tail.prev = node
        prev__.next = node 

        # update node
        node.next = self.tail
        node.prev = prev__ 

        self.count += 1
        return True
        

    def deQueue(self) -> bool:
        # early return
        if not self.count:
            return False

        top = self.head.next 

        # update queue pointers
        self.head.next = top.next
        top.next.prev = self.head
        
        # disengage pointers
        top.next = None
        top.prev = None

        self.count -= 1

        return True

    def Front(self) -> int:
        if not self.count:
            return -1

        return self.head.next.val
        

    def Rear(self) -> int:
        if not self.count:
            return -1
        
        return self.tail.prev.val
        

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count != 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()