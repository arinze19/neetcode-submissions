class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = [] 

        def dfs(index, total, path): 
            # base case 
            if total > target or index >= len(nums):
                return

            if total == target:
                res.append(path[:])
                return

            # add current item
            path.append(nums[index])
            dfs(index, total + nums[index], path)

            # remove current item
            path.pop()
            dfs(index + 1, total, path)

        dfs(0, 0, [])

        return res