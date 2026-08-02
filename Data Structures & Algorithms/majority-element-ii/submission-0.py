from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) / 3
        res = []
        freq = Counter(nums)

        print(freq)

        for key, value in freq.items():
            if value > threshold:
                res.append(key)

        return res

        

