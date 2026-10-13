class MyStack:

    def __init__(self):
        self.main_queue = deque()
        self.back_queue = deque()

    def push(self, x: int) -> None:
        self.main_queue.append(x)

    def pop(self) -> int:
        while True:
            x = self.main_queue.popleft()
            if not self.main_queue:
                self.main_queue, self.back_queue = self.back_queue, self.main_queue
                return x
            self.back_queue.append(x)

    def top(self) -> int:
        while True:
            x = self.main_queue.popleft()
            self.back_queue.append(x)
            if not self.main_queue:
                self.main_queue, self.back_queue = self.back_queue, self.main_queue
                return x

    def empty(self) -> bool:
        return not self.main_queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()