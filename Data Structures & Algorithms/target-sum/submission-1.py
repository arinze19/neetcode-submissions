class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # return the number of different ways you can build the express
        # such that the total sum equals target 

        # do we need to operate on all input numbers for the final answer [yes]
        res = 0

        if not nums:
            return 0

        def dfs(index, currentSum):
            nonlocal res

            # base case 
            if index == len(nums) - 1:
                if currentSum == target:
                    res += 1
                return
            
            # positive case 
            dfs(index + 1, currentSum + nums[index + 1])

            # negative case 
            dfs(index + 1, currentSum - nums[index + 1])

        dfs(-1, 0)

        return res