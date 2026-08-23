class MyCircularQueue:
    '''
    Keywords
    1. Ring Buffer
    2. 

    Questions
    1. Trying to enqueue an item once the queue is full results in False
    2. size of buffer is at least 1
    3. can there be duplicate values? Yes 
    4. can queue be empty when we call Front? Yes

    Thought Process
    1. enqueue -> (start + size) % capacity -> (1 + 2) % 3 | keep a start pointer
    2. isFull -> return size == capacity
    3. isEmpty -> return size
    4. Rear -> (start + (size - 1)) % capacity
    5. Front -> start
    '''

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.queue = [-1] * k
        self.start = 0
        

    def enQueue(self, value: int) -> bool:
        next__ = (self.start + self.size) % self.capacity

        # if queue position is occupied, return false
        if self.queue[next__] != -1:
            return False 

        self.queue[next__] = value
        self.size += 1

        return True
        

    def deQueue(self) -> bool:
        # if queue is empty, return False
        if self.isEmpty():
            return False 

        next__ = (self.start + 1) %  self.capacity # get next head index

        self.queue[self.start] = -1
        self.start = next__
        self.size -= 1

        return True
        

    def Front(self) -> int:
        return self.queue[self.start]
        

    def Rear(self) -> int:
        target = (self.start + (self.size - 1)) % self.capacity
        return self.queue[target]
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()