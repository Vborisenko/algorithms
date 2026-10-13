class StockSpanner:
    def __init__(self):
        self.stack = []
        self.prices = []
        self.i = -1 # to get the first incremented index as 0

    def next(self, price: int) -> int:
        self.i += 1
        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()
        res = self.i + 1 if not self.stack else self.i - self.stack[-1]
        self.stack.append(self.i)
        self.prices.append(price)
        return res
