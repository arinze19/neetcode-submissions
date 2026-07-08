class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        '''
        Questions 

        Thought process 
        1. add/ignore characters 
        2. add/ignore adding dots
        3. backtrack through possible solutions 
        4. create is_valid function 
        5. base case - when lee

        Time and Space
        time | O(n!)
        space | O(n)
        '''
        res = []

        def is_valid(path):
            if len(path) != 4:
                return False


            for identifier in path:
                if len(identifier) > 1 and identifier[0] == "0":
                    return False

                if int(identifier) < 0 or int(identifier) > 255:
                    return False

            return True

        def backtrack(i, path):
            # base case 
            if i == len(s):
                if is_valid(path):
                    res.append(".".join(path))

                return 

            for j in range(i + 1, len(s) + 1):
                path.append(s[i:j])
                backtrack(j, path)
                path.pop()

        backtrack(0, [])

        return res
        
