from collections import Counter 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        # create a frequency map of each character in both s and t
        freq_s = Counter(s)
        freq_t = Counter(t)


        for char in freq_s:
            if freq_s[char] != freq_t[char]:
                return False

        return True

        
