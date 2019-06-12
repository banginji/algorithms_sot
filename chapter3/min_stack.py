from datastructures import stack


class MinStack(stack.Stack):
    def __init__(self):
        super().__init__()

    def push(self, data):
        if self._len_stack() is 0:
            super().push((data, data))
            return
        super().push((data, self._min(data)))

    def _min(self, data):
        _, prev_min = self.peek()
        if data < prev_min:
            return data
        else:
            return prev_min


if __name__ == '__main__':
    stack = MinStack()
    stack.push(1)
    stack.push(4)
    stack.push(1)
    stack.push(6)
    stack.push(9)
    stack.push(-11)
    stack.print_stack()
    stack.pop()
    stack.pop()
    stack.print_stack()