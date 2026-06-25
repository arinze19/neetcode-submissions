class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        Questions 
        1. can needle be longer than the haystack?? Yes
        

        Thought process
        1. loop from 0 
        2. slice out word
        3. compare with needle
        4. if there is a match, return index
        5. return -1

        runtime | O(n)
        space | O(1)
        '''
        n = len(needle)
        
        for i in range(len(haystack)):
            if needle == haystack[i:i+n]:
                return i

        return -1