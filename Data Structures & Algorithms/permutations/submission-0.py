class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
       # loop through??
       # index, remaining (options to choose from), path (current perm)
       # how about we go backwards and forwards
       # base case 
       #   - len(path) == len(nums)
       #   - index < 0 or index == len(nums)
       # res = dfs() + dfs() (we include the index on the second instance)
        res = []
       
        def dfs(path, options):
            nonlocal res

            # base case
            if len(path) == len(nums):
                res.append(path[:])
                return

            for index, option in enumerate(options):
                path.append(option)
                dfs(path, options[:index] + options[index + 1:])
                path.pop()

        dfs([], nums)

        return res