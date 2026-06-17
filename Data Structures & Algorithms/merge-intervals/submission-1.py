class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        Questions
        1. are the intervals sorted by start time?
        
        Thought process
        1. loop through the intervals and add to a list
        2. if overlapping, replace prev end with appropriate end
        '''
        res = []

        intervals.sort()

        for start, end in intervals:
            if res and res[-1][1] >= start:
                res[-1][1] = end if end >= res[-1][1] else res[-1][1]
            else:
                res.append([start, end])

        return res