class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = s.strip()

        right = left = len(res) - 1

        while left >= 0 and res[left] != " ":
            left -= 1

        return right - left