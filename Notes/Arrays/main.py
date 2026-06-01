

def nextGreater(arr):
    stack = []
    
    res = [-1] * len(arr)
    
    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            top = stack.pop()
            
            res[top] = i
            
        stack.append(i)
        
    print(f"this is the result", res)
    print(f"this is the stack", stack)
    
    
# nextGreater([13, 8, 1, 5, 2, 5, 9, 7, 6, 12])
nextGreater([13, 8, 1, 5, 2, 5, 9])