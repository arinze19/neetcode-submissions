class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # combinations of k numbers chosen from [1,n]
        # dfs
        # - if len(path) == k
        # [1,20] - no need for a null input case 
        res = []

        def dfs(current, path):
            # base case 
            if len(path) == k:
                res.append(path[:])
                return

            
            # if current exceeded; immediate return
            if current == n:
                return

            # to our current path we want to add the next number
            path.append(current + 1)
            dfs(current + 1, path)

            # remove path
            path.pop()
            dfs(current + 1, path)
        
        dfs(0, [])
        
        return res