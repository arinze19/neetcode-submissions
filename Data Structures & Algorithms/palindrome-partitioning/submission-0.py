class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # base case if index == len(s)
        # add next item
        # if s[index] == s[index + 1]
        #   path[-1] += s[index + 1]
        #   backtrack(path, index + 1)

        #
        res = []

        def backtracking(index, path):
            # base case 
            if index == len(s):
                res.append(path[:])
                return

            for i in range(index, len(s)):
                if isPalindrome(s[index:i + 1]):
                    path.append(s[index:i+1])
                    backtracking(i + 1, path)
                    path.pop()

        def isPalindrome(chars):
            if not chars: 
                return False 

            left = 0
            right = len(chars) - 1

            while left < right:
                if chars[left] != chars[right]:
                    return False

                left += 1
                right -= 1
            
            return True

        backtracking(0, [])

        return res