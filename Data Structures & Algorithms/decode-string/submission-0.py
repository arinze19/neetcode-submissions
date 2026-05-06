from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        # INPUT AND OUTPUT
        # - input: sequence of string
        #   s is non-empty
        #   int in s are in the range 1-300
        #   lowercase english characters 

        # THOUGHT PROCESS
        # for char in s
        # add to a stack 
        # if char == ] (we know we are about to enter a suboperation)
        #   subchar = ""
        #   top = stack.pop()
        #   while top != [
        #       if top.isdigit():
        #           subchar = subchar * int(top)
        #       else:
        #           subchar += top
        #       
        #  else:
        #       stack.append(char)
        stack = []

        for char in s:
            if char == "]":
                queue = deque()
                digits = 1

                while stack and stack[-1] != "[":
                    top = stack.pop()

                    queue.appendleft(top)

                # we need to check the front if we have a digit
                if stack and stack[-1] == "[":
                    stack.pop() # removes the [

                    numbers = deque()

                    while stack and stack[-1].isdigit():
                        top = stack.pop()

                        numbers.appendleft(top)

                    nums = "".join(list(numbers))

                    if nums: # if there is a number in the queue
                        digits = int(nums)

                stack += digits * list(queue)
            else:
                stack.append(char)

        
        return "".join(stack)