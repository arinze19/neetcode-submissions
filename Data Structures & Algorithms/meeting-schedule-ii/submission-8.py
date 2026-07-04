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
        '''
        res = 0
        intervals = [[intervals[i].start, intervals[i].end] for i in range(len(intervals))] # O(n)
        intervals.sort() # O(n log n)
        times = []

        for start, end in intervals:
            # start = intervals[i].start
            # end = intervals[i].end

            snapshot = []

            for s, e in times:
                if e > start:
                    snapshot.append([s,e])

            snapshot.append([start, end])

            times = snapshot[:]

            res = max(len(times), res)

        return res

        '''
        ========== OPTIMIZED ==========
        # runtime | O(n log n) + O(n log n)
        # space | O(n) + O(n)
        intervals = [[intervals[i].start, intervals[i].end] for i in range(len(intervals))] # O(n)
        intervals.sort() # O(n log n)
        res = 0
        heap = []

        for start, end in intervals: # O(n)
            # while top of heap < start
            while heap and heap[0][0] <= start: # O(log n)
                heapq.heappop(heap)

            heapq.heappush(heap, (end, start)) # O(log n)

            res = max(len(heap), res)

        return res
        '''

        '''
        ========= TESTING ============
        meetings = []
        stack = []

        for interval in intervals:
            meetings.append([interval.start, interval.end])

        meetings.sort(key=lambda x: x[1])

        for start, end in meetings:
            if not stack:
                stack.append([start, end])
            else:
                s_top, e_top = stack[-1]
                if start >= e_top:
                    stack.pop()
                stack.append([start, end]) 

            print(stack, (start, end))      
        return len(stack) 
        '''