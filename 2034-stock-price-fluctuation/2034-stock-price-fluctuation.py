from sortedcontainers import SortedList
class StockPrice:

    def __init__(self):
        self.records = {}
        self.maxTimeStamp = 0
        self.prices = SortedList()
        

    def update(self, timestamp: int, price: int) -> None:
        
        if timestamp in self.records:
            origPrice = self.records[timestamp]
            #log(n) time
            self.prices.remove(origPrice)
        #log(n) time    
        self.prices.add(price)
        self.records[timestamp] = price
        self.maxTimeStamp = max(self.maxTimeStamp, timestamp)
        

    def current(self) -> int:
        #O(1) time
        return self.records[self.maxTimeStamp]

    def maximum(self) -> int:
        #log(n) time
        return self.prices[-1]

    def minimum(self) -> int:
        #log(n) time
        return self.prices[0]