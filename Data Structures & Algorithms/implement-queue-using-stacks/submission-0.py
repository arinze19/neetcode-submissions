class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    # push -> push directly unto the in stack
    # pop -> if out stack is empty, tranfer in stack to out stack and pop
    # peek -> if out stack is empty, transfer in stack to out stack and peek
    # empty -> if both stack are empty
    # [5,6,7]
    # [3,2,1]

    # [[], [1], [2]]
    # [4,5]
    # [2,1]
    def _transfer(self):
        if not self.out_stack:
            while self.in_stack:
                top = self.in_stack.pop()

                self.out_stack.append(top)

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._transfer()

        if self.empty():
            raise KeyError("Queue is empty")

        return self.out_stack.pop()
        
    def peek(self) -> int:
        self._transfer()

        if self.empty():
            raise KeyError("Queue is empty")

        return self.out_stack[-1]
        

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()