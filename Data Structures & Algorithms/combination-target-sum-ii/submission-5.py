class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # base case 
        # if currentSum == target: add to the array and return

        # if currentSum > target or index >= len(candidates)

        # add to the running sum

        # do not add to the running sum
        candidates.sort() 

        res = []
        
        def dfs(path, currentSum, index):
            if currentSum == target:
                res.append(path[:])
                return

            if currentSum > target or index >= len(candidates):
                return

            # add item
            path.append(candidates[index])
            dfs(path, currentSum + candidates[index], index + 1)

            # remove item
            path.pop()
            index += 1
            while index < len(candidates) and index >= 0 and candidates[index] == candidates[index - 1]:
                index += 1
            dfs(path, currentSum, index)

        dfs([],0,0)

        return res
        """
        candidates = [1,2] | target = 3
        res = []

        # ([],0,0) | current count and running sum
        # first iteration
        
        # left side (1)
        # ([1],1,1)
        
        # left side (2)
        # ([1,2],3, 2)
        

        # right side (2)
        # ([1],1,2)

        # right side (1)
        # ([],0,2)

        Edge case for empty set
        """