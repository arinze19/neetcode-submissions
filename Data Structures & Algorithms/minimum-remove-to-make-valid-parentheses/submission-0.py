class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i, char in enumerate(s):
            if char != ")" and char != "(":
                continue

            if stack and s[stack[-1]] == "(" and char == ")":
                stack.pop()
            else:
                stack.append(i)

        cache = set(stack)
        res = ""

        for i, char in enumerate(s):
            if i not in cache:
                res += char

        return res