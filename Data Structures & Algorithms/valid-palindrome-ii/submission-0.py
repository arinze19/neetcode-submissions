class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        with at most room for one error

        Questions 
        1. can we have empty string? No
        2. 
        '''
        count = 1

        def validPalindromeHelper(s):
            print(s)
            nonlocal count

            if not s:
                return True

            if s[0] == s[len(s) - 1]:
                return validPalindromeHelper(s[1:len(s) - 1])
            elif s[0] != s[len(s) - 1] and count:
                count -= 1
                return validPalindromeHelper(s[:len(s) - 1]) or validPalindromeHelper(s[1:])
            
            return False

        return validPalindromeHelper(s)