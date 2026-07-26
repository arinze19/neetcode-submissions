from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque([])

        # loop through the input 
        # [1,2,3,4] | k = 2
        # i = 0 | [0] | []
        # i = 1 | [1] | [1]
        # i = 2 | [2] | [2,3]
        # i = 3 | [3] | [2,3,4]

        for i in range(len(nums)):
            # remove top item if out of range
            # why is less than or equal to (I guess to indicate that the window is full)
            while queue and queue[0] <= i - k:
                queue.popleft()

            # remove previous items less than current index
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()

            queue.append(i)

            # we only want to add to the result when we have reach a certain index 
            if i >= k - 1: # this starts from the edge of the window
                res.append(nums[queue[0]])

        return res

        