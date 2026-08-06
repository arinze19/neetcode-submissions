class BrowserHistory:
    '''
    Keywords
    1. start at homepage 
    2. move forward and backward "step" number of times
    3. forward clears up all forward history
    4. you can move back x number of steps back if steps > x (hard limit)
    5. you can move forward x number of steps if steps > x (hard limit)

    Questions 
    1. can we visit two pages of the same website consecutively? Yes
    2. can we go back if the stack is empty? Yes, return an empty string perhaps (we can never reach this state)

    Thought Process
    1. Stack/Cursor to keep track of current page
    2. Linked List? 
    '''

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.cursor = 0
        

    def visit(self, url: str) -> None:
        self.stack = self.stack[:self.cursor + 1] # remove pages forward from the cursor
        self.stack.append(url)
        self.cursor = len(self.stack) - 1 # reset cursor to point to the latest entry


    def back(self, steps: int) -> str:
        # [neetcode.com, google.com linkedin.com]
        # steps = 1
        if self.cursor - steps < 0:
            self.cursor = 0
        else:
            self.cursor -= steps

        return self.stack[self.cursor]
        

    def forward(self, steps: int) -> str:
        if steps + self.cursor >= len(self.stack):
            self.cursor = len(self.stack) - 1
        else:
            self.cursor += steps

        return self.stack[self.cursor]
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)