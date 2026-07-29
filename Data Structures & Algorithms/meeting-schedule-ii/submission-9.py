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
        points = []
        count = 0
        max_ = 0

        for node in intervals:
            points.append([node.start, +1])
            points.append([node.end, -1])

        points.sort()

        for point, increment in points:
            count += increment 
            max_ = max(max_, count)
        
        return max_