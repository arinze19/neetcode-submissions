from collections import Counter
from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        - add the frequencies of t in a counter
        - loop through chars of s
            * for each encounter, reduce frequency in t
            * once limit is reached, try to close window and compare freq
                while window is still valid, recalculate min
            i = 0
            j = 8
            (j - i + 1)
        """
        t_freq = Counter(t)
        s_freq = defaultdict(int)

        j = 0
        count = 0
        res = [-1, -1]
        mini = float("inf")

        for i in range(len(s)):
            s_freq[s[i]] += 1

            if s[i] in t_freq and s_freq[s[i]] == t_freq[s[i]]:
                count += 1

            while count == len(set(t)):
                if mini > i - j + 1:
                    mini = i - j + 1
                    res = [j, i + 1]

                s_freq[s[j]] -= 1

                if s_freq[s[j]] < t_freq[s[j]]:
                    count -= 1
                
                j += 1
        
        
        return s[res[0]:res[1]]


