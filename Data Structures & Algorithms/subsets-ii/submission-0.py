class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        
        def dfs(index, path):
            # base case 
            if index == len(nums):
                res.append(path[:])
                return

            if index > len(nums):
                return

            # recursive case: add 
            path.append(nums[index])
            dfs(index + 1, path)

            # recursive case: remove
            path.pop()
            while index + 1 < len(nums) and nums[index + 1] == nums[index]:
                index += 1
            dfs(index + 1, path)

        dfs(0, [])

        return res

            
