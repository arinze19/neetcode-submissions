"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import deque 
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        '''
        Questions 
        1. interval can be empty
        2. 

        Thought process
        1. add the intervals into a stack
        2. get the max of the stack 
        3. return the max of the stack

        Thought process (optimized)
        1. loop through intervals
        2. add item to a maxHeap
        3. while start time of incoming > end time of top
            - pop top
        4. insert item
        5. take max(res, len(heap))

        edge case
        1. track the max(start)
        2. track the min(end)


        '''

        '''
        ========== BRUTE FORCE ==========
        res = 0
        queue = deque([])

        for i in range(len(intervals)):
            start = intervals[i].start
            end = intervals[i].end

            while queue and queue[-1][1] <= start:
                queue.pop()

            while queue and queue[0][1] <= start:
                queue.popleft()

            queue.append([start, end])

            res = max(len(queue), res)

        return res
        '''

        intervals = [[intervals[i].start, intervals[i].end] for i in range(len(intervals))]
        intervals.sort()
        res = 0
        heap = []

        for start, end in intervals:
            # while top of heap < start
            while heap and heap[0][0] <= start:
                heapq.heappop(heap)

            heapq.heappush(heap, (end, start))

            res = max(len(heap), res)

        return res