class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        Questions 
        1. n cannot be 0 
        
        Thought Process 
        1. n pairs of parentheses 
        2. state -> open & close brackets count
            - open -= 1
            - how to prevent an invalid state (prune)
            - if close < open -> prune? 
            - if open <= 0 -> prune
        '''
        res = []
        count_cache = { "(": n, ")": n }

        def backtrack(path, cache):
            # success case 
            if cache[")"] == 0 and cache["("] == 0:
                res.append("".join(path))
                return 

            # recursive case 
            for bracket in list(cache.keys()):
                path.append(bracket)
                cache[bracket] -= 1

                if cache[")"] >= cache["("] and cache["("] >= 0 and cache[")"] >= 0:
                    backtrack(path, cache)

                cache[bracket] += 1
                path.pop()

        backtrack([], count_cache)

        return res 
