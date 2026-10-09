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
        KEYWORDS 
        1. minimum number of rooms to schedule meetings without conflict 

        QUESTIONS 
        1. interval can be empty? Yes 
        2. intervals sorted? No

        THOUGHT PROCESS 
        1. use a sweep line algorithm to account for currently occupied rooms

        RUNTIME 
        1. space | O(n)
        2. time | O(n)
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