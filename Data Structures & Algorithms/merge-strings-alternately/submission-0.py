class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        res = ""

        while left < len(word1) and right < len(word2):
            select = (left + right) % 2

            if select == 0:
                res += word1[left]
                left += 1
            else:
                res += word2[right]
                right += 1

        # if word1 left over 
        if left < len(word1):
            res += word1[left:]

        # if word2 left over 
        if right < len(word2):
            res += word2[right:]

        return res 
