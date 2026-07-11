from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''
        Questions 
        1. letters can be shuffled (s can change)
        2. s characters are case sensitive
        3. s cannot be empty
        4. can there be cases where there are not palindromes

        Thought process 
        1. even/odd length palindrome
        2. count the pairs of each characters
        3. if len(s) == odd ? count + 1 : count
        
        ab
        aba
        '''
        # sort the array
        # 
        count = 0
        word = list(s)
        stack = []

        word.sort()

        for char in word:
            if stack and stack[-1] == char:
                stack.pop()
                count += 2
            else:
                stack.append(char)

        # if len(stack) != 0 - return count + 1
        return count + 1 if stack else count