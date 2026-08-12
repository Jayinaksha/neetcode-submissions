class MinStack:

    def __init__(self):
        self.stack=collections.deque()
        self.min=collections.deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        current_min = self.min[-1] if self.min else val
        self.min.append(min(val,current_min))

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
