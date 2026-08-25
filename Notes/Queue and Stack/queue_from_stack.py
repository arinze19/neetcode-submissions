class QueueFromStack:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []
    
    def push(self, val):
        self.in_stack.append(val)
        
    # in -> [4,5]
    # out -> [1]
    def pop(self):
        # if not 
        if not self.out_stack:
            while self.in_stack:
                top = self.in_stack.pop()
                
                self.out_stack.append(top)
                
        if not self.out_stack and not self.in_stack:
            return -1
        
        return self.out_stack.pop() 
    
    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                top = self.in_stack()
                
                self.out_stack.append(top)
                
        if not self.out_stack and not self.in_stack:
            return -1
                
        return self.out_stack[-1]
    
    def empty(self):
        return not self.in_stack and not self.out_stack