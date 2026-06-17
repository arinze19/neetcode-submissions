"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        updated_intervals = []
        stack = []

        if len(intervals) <= 1:
            return True

        for i in range(len(intervals)):
            interval = intervals[i]

            updated_intervals.append([interval.start, interval.end])

        updated_intervals.sort() # O(n log n)

        for i in range(len(updated_intervals) - 1): # O(n)
            j = i + 1
            if updated_intervals[i][1] > updated_intervals[j][0]:
                return False

        return True
