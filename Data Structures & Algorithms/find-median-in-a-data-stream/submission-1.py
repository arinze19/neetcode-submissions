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
        
        
        