from collections import deque

class MyStack:
    # maintain two queues? 
    # push: add to end of queue 
    # pop: 
    #       - rotate, get first item
    #       - we already are back to the original order
    # top:
    #       - rotate, get first item
    #       - shift first item to the back
    # empty: 
    #       - if queue length is none

    def __init__(self):
        self.queue = deque([])

    def _rotate(self):
        size = len(self.queue)

        # reverse all elements right up until the last element
        # with last element being at the front
        for item in range(size - 1):
            top = self.queue.popleft()

            self.queue.append(top)

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        # reverse so last item is first item
        self._rotate()

        return self.queue.popleft()
        
    def top(self) -> int:
        # reverse so last item is first item
        self._rotate()

        val = self.queue[0]

        # move back
        for _ in range(1):
            top = self.queue.popleft()

            self.queue.append(top)

        return val

    def empty(self) -> bool:
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()