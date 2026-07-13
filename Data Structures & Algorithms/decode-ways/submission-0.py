class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        Questions 
        1. One based (Not zero indexed)
        2. 

        Thought process
        1. backtrack [done]
        2. top-down 
        '''

        mappings = {
            "1": "A",
            "2": "B",
            "3": "C",
            "4": "D",
            "5": "E",
            "6": "F",
            "7": "G",
            "8": "H",
            "9": "I",
            "10": "J",
            "11": "K",
            "12": "L",
            "13": "M",
            "14": "N",
            "15": "O",
            "16": "P",
            "17": "Q",
            "18": "R",
            "19": "S",
            "20": "T",
            "21": "U",
            "22": "V",
            "23": "W",
            "24": "X",
            "25": "Y",
            "26": "Z"
        }

        n = len(s)

        count = 0

        memo = {}

        def is_valid(char):
            if len(char) > 2 or char not in mappings or char[0] == "0":
                return False

            return True

        def backtrack(i):
            count = 0

            if i in memo:
                return memo[i]

            # base case 
            if i == n:
                memo[i] = 1
                return memo[i]

            # expand to at most 2 chars
            for j in range(i, min(n, i + 2)):
                char = s[i:j + 1]

                if is_valid(char):
                    count += backtrack(j + 1)
            
            memo[i] = count
            return count

        return backtrack(0)




