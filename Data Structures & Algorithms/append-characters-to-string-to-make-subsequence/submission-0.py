class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # lowercase characters 

        # count of characters needed to add to s; so
        # t becomes a subsequence of s

        # Thought Process 
        # if len(t) < len(s): return False
        # scan through the items in s to identify the values we have in t
        # scan through to identify the values we need to add to s
        j = 0
        for i in range(len(s)):
            if j < len(t) and s[i] == t[j]:
                j += 1

        return len(t) - j