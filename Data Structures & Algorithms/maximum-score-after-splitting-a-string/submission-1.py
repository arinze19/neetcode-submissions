class Solution:
    def maxScore(self, s: str) -> int:
        '''
        KEYWORDS
        1. number of zeros on the left 
        2. number of ones on the right 

        Questions 
        1. There are only 0's and 1's in the string? Yes 
        2. String length is at least 2? Yes 

        Thought process 
        1. loop throug the string (quadratic)
            - partition the string into left and right 
            - count the number of 0's and 1's 
            - O(n^2) | O(1)
        2. keep count of no of 1's (linear)
            - 4
            loop through 
            - if s[i] == "0":
                add to the left side 
            - if s[i] == "1":
                remove from the right side 

            011101
            left = 1
            right = 1

            - O(n) | O(1)
        '''
        left = 0
        right = 0
        res = 0

        for char in s:
            if char == "1":
                right += 1

        for i in range(len(s) - 1):
            char = s[i] # get char 

            if char == "1":
                right -=1 
            else:
                left += 1

            res = max(res, right + left)

        return res

            
            


