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

        runtime | O(H * n)
        space | O(1)
        '''

        i = 0

        while i < len(haystack):
            left = i
            right = 0
            while right < len(needle) and left < len(haystack) and haystack[left] == needle[right]:
                right += 1
                left += 1

            if right == len(needle):
                return i

            i += 1

        return -1


        