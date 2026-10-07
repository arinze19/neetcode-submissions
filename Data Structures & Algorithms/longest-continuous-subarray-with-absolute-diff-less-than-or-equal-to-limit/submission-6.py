from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        '''
        - sliding window + hash_map? 
        - sliding window + heap
        - sliding window + queue
        - how to figure out which queue to popleft from?

        min_queue = [(5,1),(6,2)] 
        max_queue = [(6,2)]
        right = 0
        left = 0
        res = 2

        run calculations before adding to queue

        while min_queue and incoming < min_queue[0]:
            min_queue.popleft()

        min_queue.append(incoming)

        while max_queue and incoming > max_queue[0]:
            max_queue.popleft()

        max_queue.append(incoming)

        while abs(min_queue[0][0] - max_queue[0][0]) > k:
            if min_queue[0][1] < max_queue[0][1]:
                min_queue.popleft()
            else:
                max_queue.popleft()
            left += 1

        res = max(res, right - left + 1)

        return res

        - how to manage left
        '''
        res = 0
        left = 0
        max_queue = deque([])
        min_queue = deque([])

        for right in range(len(nums)):
            # add to min_queue 
            while min_queue and min_queue[-1][0] > nums[right]:
                min_queue.pop()

            min_queue.append((nums[right], right))

            # add to max_queue 
            while max_queue and max_queue[-1][0] < nums[right]:
                max_queue.pop()

            max_queue.append((nums[right], right))

            while abs(min_queue[0][0] - max_queue[0][0]) > limit:
                # get bounding
                if min_queue[0][1] < max_queue[0][1]:
                    left = min_queue.popleft()[1] + 1
                else:
                    left = max_queue.popleft()[1] + 1

            res = max(res, right - left + 1)

        return res
        




