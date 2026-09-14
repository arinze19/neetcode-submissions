class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        KEYWORDS 
        1. space separated sequence of one or more words 
        2. you are allowed to reuse dictionary words 

        QUESTIONS 
        1. we have to use all words in the wordDict to form a word? No 
        2. can we have duplicates in the wordDict? No
        3. can strings be empty? No
        4. can we have empty string in the wordDict? No

        THOUGHT PROCESS
        0. backtracking
        1. base case 
            - i > len(s)
              return True
        2. function call 
            - backtrack(i)
                for j in range(i, len(s) + 1): #O(n)
                    if s[i:j] in wordDictSet: # O(n)
                        if backtrack(j):
                            return True

                return False
        3. return backtrack(0)

        TIME AND SPACE 
        1. time | O(n^2) wrong | O(2^n)
        2. space | O(n) ~ we can go a level deep for all characters 
        '''
        cache = set(wordDict)

        def backtrack(i, memo):
            # base case 
            if i >= len(s):
                return True 

            if i in memo:
                return memo[i]

            memo[i] = False

            # validate 
            for j in range(i, len(s) + 1):
                substring = s[i:j]

                if substring in cache and backtrack(j, memo):
                    memo[i] = True

            return memo[i]

        return backtrack(0, {})