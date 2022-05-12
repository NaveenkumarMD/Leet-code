from collections import deque

class MyStack:

    def __init__(self):
        self._stack = deque()

    def push(self, x: int) -> None:
        self._stack.append(x)

    def pop(self) -> int:
        return self._stack.pop()

    def top(self) -> int:
        return self._stack[-1]        

    def empty(self) -> bool:
        return len(self._stack) == 0