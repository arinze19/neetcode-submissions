from collections import deque 

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        '''
        Questions 
        1. are the strings sorted? 
        stack:
            - (char, neededTime)
            - sliding window 
                - if s[i] == s[j]
                - remove minimum
                repeat until j out of bound 
                - return count 
                - use a deque to convert to constant time removal 
        '''
        queue = deque([])
        count = 0

        for color, time in zip(colors, neededTime):
            queue.append((color, time))

        while queue:
            current_color, current_time = queue.popleft()

            while queue and current_color == queue[0][0]:
                next_color, next_time = queue.popleft()

                count += min(next_time, current_time)
                current_time = max(next_time, current_time)

        return count 
        

        

