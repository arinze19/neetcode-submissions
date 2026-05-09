class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(index, path):
            # base case 
            if index >= len(nums):
                res.append(path[:])
                return

            # recursive case 

            # add decision
            path.append(nums[index])
            dfs(index + 1, path)

            # remove desicion
            path.pop()
            dfs(index + 1, path)

        dfs(0, [])

        return res

        # [1]

        
