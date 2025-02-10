class StockSpanner:

    def __init__(self):
       self.stack = [] 
       self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        # print(self.prices)
        # print(self.stack)
        result = 1
        while self.stack and self.prices[self.stack[-1]] <= price:
            ele = self.stack.pop()
        
        if self.stack:
            result = len(self.prices)-self.stack[-1]-1
        else:
            result = len(self.prices)
        
        self.stack.append(len(self.prices)-1)
        # print(self.stack)
        # print(result)
        # print("----")
        return result




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)