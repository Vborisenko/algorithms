class FreqStack:
    def __init__(self):
        self._freq_stack = defaultdict(lambda: [])
        self._frequency_map = defaultdict(lambda: 0)
        self.current_max = 0

    def push(self, val: int) -> None:
        self._frequency_map[val] += 1
        self.current_max = max(self.current_max, self._frequency_map[val])
        self._freq_stack[self._frequency_map[val]].append(val)

    def pop(self) -> int:
        if stack := self._freq_stack.get(self.current_max):
            candidate = stack.pop()
        else:
            self.current_max -= 1
            return self.pop()
        self._frequency_map[candidate] -= 1
        return candidate