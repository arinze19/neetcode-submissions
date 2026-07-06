class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix sum
        # [0, 1, 2, 8]
        # [48,24,6,0]
        n = len(nums)
        left = [1] * n
        right = [1] * n
        res = [1] * n
        total = 1
        
        # if we loop through we prefix sum the trailing items
        for i in range(n):
            # insert the total first 
            left[i] = total
            total = total * nums[i]

        # reset total
        total = 1

        for j in range(n - 1, -1, -1):
            right[j] = total
            total = total * nums[j]

        for k in range(n):
            res[k] = left[k] * right[k]

        return res



        