class Solution:
    def scoreOfString(self, s: str) -> int:
        # can string be odd??
        # sliding window
        res = 0

        for i in range(1, len(s)):
            res += abs(ord(s[i]) - ord(s[i - 1]))

        return res
