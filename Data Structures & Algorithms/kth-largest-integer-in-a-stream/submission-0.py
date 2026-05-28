import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums) # heapify input 

        self.cache = nums
        self.limit = k
        

    def add(self, val: int) -> int:
        heapq.heappush(self.cache, val)
        return heapq.nlargest(self.limit, self.cache)[-1]