class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

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
    1. Stack/Cursor to keep track of current page [done]
    2. Linked List? 
        - initialize history with a dummy node(homepage)
        - initialize a variable (curr, this is the current node we are at)
        visit:
            - add a node to curr as the next node
            - upate curr to curr.next
        back:
            - while steps and curr.prev:
                curr = curr.prev
                steps -= 1
        forward:
            - while steps and curr.next:
                curr = curr.next
    '''

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    # neetcode, google, facebook. youtube

    def visit(self, url: str) -> None:
        node = Node(url) # create node 

        # upate node variables
        node.prev = self.curr
        self.curr.next = node

        self.curr = node # move pointer forward

    def back(self, steps: int) -> str:
        while self.curr.prev and steps:
            self.curr = self.curr.prev
            steps -= 1

        return self.curr.val        

    def forward(self, steps: int) -> str:
        while self.curr.next and steps:
            self.curr = self.curr.next 
            steps -= 1

        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)