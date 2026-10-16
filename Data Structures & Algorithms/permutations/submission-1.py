class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        - loop through num in nums
        - for each num, mark as used 
        - loop through num and pick out values that are not used 
        - base case? len(path) == len(nums)
        '''
        used = [False] * len(nums)
        res = []
        path = []

        def backtrack():
            # base case 
            if len(path) == len(nums):
                res.append(path[:])
                return 

            for i in range(len(nums)):
                # if current item is already used
                if used[i]:
                    continue 

                # set used
                used[i] = True
                path.append(nums[i])

                backtrack()

                used[i] = False
                path.pop()
                
        backtrack()

        return res

