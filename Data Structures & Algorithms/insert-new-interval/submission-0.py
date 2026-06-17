class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = []
        
        intervals.append(newInterval) # O(n)

        intervals.sort() # O(n log n)

        for start, end in intervals: #O (n)
            if stack and stack[-1][1] >= start:
                stack[-1][1] = end if end >= stack[-1][1] else stack[-1][1]
            else:
                stack.append([start, end])

        return stack


            