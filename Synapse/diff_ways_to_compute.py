
def diffWaysToCompute(expression) :
    # find first instance of operation
    # backtrack(i + 1, expression) - do not take expression
    # backtrack(i + 1, expression) - take expression

    # base case - if there is no operation, add the expression into the res

    # how to validate expression
    # join left and right of operation and add back to the expression
    # also count for alphanumeric characters that are lined side by side 

    # space and time 
    # space | O(n)
    # time | O(n!)

    # filter the expression for non-alphabetic characters 
    # 
    res = []

    def backtracking(expression):
        
        operations = [(index, char) for index, char in enumerate(expression) if not char.isdigit()]

        # base case 
        if not operations or (len(operations) == 1 and operations[0][0] == 0): # To account for negative numbers??
            res.append(int(expression))
            return 

        # recusive case 
        for index, operation in operations:
            left = index
            right = index
            
            # add operation
            while left - 1 >= 0 and expression[left - 1].isdigit():
                left -= 1

            while right + 1 < len(expression) and expression[right + 1].isdigit():
                right += 1


            leftCount = int(expression[left:index])
            rightCount = int(expression[index + 1:right + 1])
            count = 0
            
            

            if operation == "+":
                count = leftCount + rightCount
            elif operation == "-":
                count = leftCount - rightCount
            else:
                count = leftCount * rightCount
                

            backtracking(expression[:left] + str(count) + expression[right + 1:])
    
    backtracking(expression)
    
    return res

# print(diffWaysToCompute('2-1-1'))
print(diffWaysToCompute('2*3-4*5'))