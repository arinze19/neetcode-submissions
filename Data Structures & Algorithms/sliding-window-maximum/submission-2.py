from collections import deque 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Keywords
        1. window of size k 
        
        Questions 
        1. k <= nums.length
        2. negatives are allowed 
        3. duplicate items in the nums

        Thought Process
        1. queue - remove from the front once window is out of scope
        2. monotonic decreasing stack to keep track of the max item in range
        3.  queue - [4,5,6]
            stack - [6]

            sub-problems:
            1. how do we start adding to the max result
                - once size of queue is == k
                - get the max item from the front of the stack
            2. how do we pop out of the queue
                - add new item to stack
                    while stack and stack[-1] < nums[i]
                        * popleft()
                -
                - if len(queue) > k:
                    remove from the front
                    if item at the front is the same as the item on the stack we pop from the stack

        Time/Space Complexity
        time | O(n)
        space | O(n)
        '''
        queue = deque()
        monotonic_deque = deque() # monotonically non-decreasing deque
        res = []

        # queue - [4,5,6]
        # monotonic_deque - [6]
        # res - [2,2,4,4,6]

        for i in range(len(nums)):
            queue.append(i) 

            # add to stack
            while monotonic_deque and nums[monotonic_deque[-1]] < nums[i]:
                monotonic_deque.pop()

            monotonic_deque.append(i)

            # if size is greater 
            if len(queue) > k:
                top = queue.popleft()

                if top == monotonic_deque[0]:
                    monotonic_deque.popleft()

            # if size == k
            if len(queue) == k:
                res.append(nums[monotonic_deque[0]])

        return res


