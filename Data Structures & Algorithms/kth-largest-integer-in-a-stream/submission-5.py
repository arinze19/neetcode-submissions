import heapq

class KthLargest:
    '''
    Keywords
    1. find kth largest in a stream of values 

    Questions 
    1. stream is sorted? No
    2. if items not up to k

    Thought Process
    1. array and sort per "add" call
        - O(n^2logn)
    2. heap
    '''

    # time | O(n)
    # space | O(n)
    def __init__(self, k: int, nums: List[int]): 
        self.heap = []
        self.capacity = k

        for num in nums: 
            heapq.heappush(self.heap, num)

            if len(self.heap) > self.capacity:
                heapq.heappop(self.heap)

    # space | O(1)
    # time | O(m * log k)
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.capacity:
            heapq.heappop(self.heap)

        return self.heap[0]
        
