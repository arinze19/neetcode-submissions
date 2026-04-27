class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initiate left and right pointers
        # while not s[left].isalnum(): left += 1
        # while not s[right].isalnum(): right -= 1
        # if s[left] != s[right]: return False
        # else: left += 1 and right -= 1
        # return False
        left = 0 
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True

        