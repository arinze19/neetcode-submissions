import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # add to the list
        # sort the list 
        # return the kth element
        nums.sort(reverse=True)

        self.cache =  nums
        self.limit = k       

    def add(self, val: int) -> int:
        self.cache.append(val)

        self.cache.sort(reverse=True)
        return self.cache[self.limit - 1]
        