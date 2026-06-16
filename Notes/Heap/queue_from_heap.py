import heapq

class Queue:
    def __init__(self):
        self.timestamp = 0
        self.queue = []
        
    def add(self, num):
        heapq.heappush(self.queue, (self.timestamp, num))
        self.timestamp += 1
        
    def remove(self):
        heapq.heappop(self.queue)
        
    def peek(self):
        return self.queue
    

queue = Queue()
queue.add(1)
queue.add(2)
queue.add(3)
print(queue.peek())