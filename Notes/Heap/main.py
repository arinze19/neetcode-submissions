import heapq

class MedianFinder:
    # space | O(n)
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    # time | O(log(size(self.maxHeap) or size(self.minHeap)))
    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        
        # if self.minHeap and self.maxHeap and self.maxHeap[0] > self.minHeap[0]
        if self.minHeap and self.maxHeap and -self.maxHeap[0] > self.minHeap[0]:
            top = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, top)

        # if len(maxHeap) - len(minHeap) >= 2
        # pop from maxHeap and give to min heap
        while len(self.maxHeap) - len(self.minHeap) >= 2:
            top = -heapq.heappop(self.maxHeap)

            heapq.heappush(self.minHeap, top)
            
        while len(self.minHeap) - len(self.maxHeap) >= 2:
            top = heapq.heappop(self.minHeap)
            
            heapq.heappush(self.maxHeap, -top)

    # time | O(1)
    def findMedian(self) -> float:
        # if left is greater than right 
        # if right is greater than left
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        
        return (self.minHeap[0] + -self.maxHeap[0]) / 2
    
    def peek(self):
        return [self.maxHeap, self.minHeap]
 
 
medianFinder = MedianFinder()

medianFinder.addNum(1)
print(medianFinder.findMedian())
medianFinder.addNum(3)
print(medianFinder.findMedian())
medianFinder.addNum(2)
print(medianFinder.findMedian())
medianFinder.addNum(8)
medianFinder.addNum(9)
medianFinder.addNum(10)
medianFinder.addNum(11)
medianFinder.addNum(12) 
  
def k_largest_in_binary_heap(A, k):
    candidates = [(-A[0], 0)]
    res = []
    
    for _ in range(k):
        value, index = heapq.heappop(candidates)
        
        res.append(-value)
        
        left = 2 * index + 1
        right = 2 * index + 2
        
        if left < len(A):
            heapq.heappush(candidates, (-A[left], left))
            
        if right < len(A):
            heapq.heappush(candidates, (-A[right], right))
            
    return res

arr = [561, 314, 401, 28, 156, 359, 271, 11, 3]
print(k_largest_in_binary_heap(arr, 5))

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
            

    
    
    
