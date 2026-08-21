class StockSpanner:

    def __init__(self):
        self.stock = []
        self.stack = []
        

    def next(self, price: int) -> int:
        while self.stack and self.stock[self.stack[-1]] <= price:
            self.stack.pop()

        self.stock.append(price)
        self.stack.append(len(self.stock) - 1)

        if len(self.stack) == 1:
            return self.stack[-1] + 1
        else:
            return self.stack[-1] - self.stack[-2]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)