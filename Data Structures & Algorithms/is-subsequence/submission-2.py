class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
       # count variable 
       # s[i] == t[j]
       # count += 1
       # i += 1
       # return len(s) == count
        count = 0
        left = 0

        if not s:
            return True

        for right in range(len(t)):
            if left < len(s) and t[right] == s[left]:
                count += 1
                left += 1

        return len(s) == count