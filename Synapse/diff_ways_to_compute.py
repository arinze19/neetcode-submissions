
def diffWaysToCompute(expression) :
        memo = {}

        def solve(text: str) -> list[int]:
            if text in memo:
                return memo[text]
            results = []
            for index, token in enumerate(text):
                if token in '+-*':
                    for left in solve(text[:index]):
                        for right in solve(text[index + 1:]):
                            if token == '+':
                                results.append(left + right)
                            elif token == '-':
                                results.append(left - right)
                            else:
                                results.append(left * right)
            if not results:
                results = [int(text)]
            memo[text] = results
            return results
        return solve(expression)

# print(diffWaysToCompute('2'))
print(diffWaysToCompute('2*3-4*5'))