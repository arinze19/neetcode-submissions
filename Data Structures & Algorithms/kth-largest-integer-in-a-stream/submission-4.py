import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # add to the list
        # sort the list 
        # return the kth element
        nums.sort()

        heapq.heapify(nums)

        if len(nums) > k:
            nums = nums[len(nums) - k:]

        self.cache =  nums
        self.limit = k       

    def add(self, val: int) -> int:
        heapq.heappush(self.cache, val)

        if len(self.cache) > self.limit:
            heapq.heappop(self.cache)

        return self.cache[0]