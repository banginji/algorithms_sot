class Stack:
    def __init__(self):
        self.stack_data = []

    def push(self, data):
        self.stack_data = [data] + self.stack_data

    def pop(self):
        popped_data = self.stack_data[0]
        self.stack_data = self.stack_data[1:]
        return popped_data

    def peek(self):
        return self.stack_data[0]

    def _len_stack(self):
        _len = 0
        while self.stack_data[_len: _len+1]:
            _len += 1
        return _len

    def print_stack(self):
        for idx in range(self._len_stack()):
            print(f"{self.stack_data[idx]}", end=", ")
        print(end="\n")