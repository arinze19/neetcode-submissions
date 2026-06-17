class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Questions
        1. is the intervals sorted?? No
        2. edge boundaries are not considered overlapping?? Yes

        Thought process
        1. create a new list with non-interlapping algorithms 
        2. return the difference
        '''
        res = []

        intervals.sort(key=lambda x: x[1])

        for i in range(len(intervals)):
            start, end = intervals[i]

            if not res or res[-1][1] <= start:
                res.append([start, end])

        return len(intervals) - len(res) 