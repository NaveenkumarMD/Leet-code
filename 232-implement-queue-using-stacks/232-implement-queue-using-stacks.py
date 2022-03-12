class MyQueue:

    def __init__(self):
        self.primary=[]
        self.secondary=[]
        

    def push(self, x: int) -> None:
        self.primary.append(x)

    def pop(self) -> int:
        while self.primary:
            self.secondary.append(self.primary.pop())
        x=self.secondary.pop()
        while self.secondary:
            self.primary.append(self.secondary.pop())
        return x

    def peek(self) -> int:
        while self.primary:
            self.secondary.append(self.primary.pop())
        x=self.secondary[-1]
        while self.secondary:
            self.primary.append(self.secondary.pop())
        return x

    def empty(self) -> bool:
        return len(self.primary)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()