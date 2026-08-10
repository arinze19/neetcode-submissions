from collections import defaultdict

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Questions 
        1. intervals are sorted? No
        2. intervals that share the same point are not considered overlapping

        Thought Process
        1. Sweeping Line (perhaps sweep line does not work for range questions) 
        2. use intervals

        TIME AND SPACE 
        1. time | O(n)
        2. space | O(n)
        '''
        stack = []
        intervals.sort(key=lambda x: x[1])

        print(intervals)

        for start, end in intervals:
            if not stack or stack and stack[-1] <= start:
                stack.append(end)

        return len(intervals) - len(stack)
