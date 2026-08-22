class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        '''
        Keywords 
        1. numbered 0 - (n - 1)
        2. height[i] represents the height of the i-th person
        3. conditions: strictly shorter 

        Questions
        1. heights are unique
        2. height has at least one element

        Thought process
        1. Brute Force: nested loop 
            -> time | O(n^2)
            -> space | O(n)
        2. Optimized: monotonic stack
            -> time | O(n)
            -> space | O(n)

            20mins
            - once we can add to the stack, we increase the count of the top of the stack
            - shorter items cannot see past if there is one taller than they are 
            [3,2,1,1,1,0]
            [11,9]
        '''
        res = [0] * len(heights)
        stack = []

        for i in range(len(heights)):
            while stack and heights[stack[-1]] < heights[i]:
                top = stack.pop()
                res[top] += 1
            
            if stack:
                res[stack[-1]] += 1 # can see current item

            stack.append(i)

        return res
        

