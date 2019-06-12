from datastructures import stack


class MyQueue():
    def __init__(self):
        self.stack_one = stack.Stack()
        self.stack_two = stack.Stack()

    def enqueue(self, data):
        self.stack_one.push(data)

    def dequeue(self):
        for item in self.stack_one.stack_data:
            self.stack_two.push(self.stack_one.pop())
        dequeued_element = self.stack_two.pop()
        for item in self.stack_two.stack_data:
            self.stack_one.push(self.stack_two.pop())
        return dequeued_element

    def print_queue(self):
        print("[", end="")
        for idx in range(self._len_queue()):
            print(f"{self.stack_one.stack_data[idx]}", end=", ")
        print("]", end="\n")

    def _len_queue(self):
        _len = 0
        while self.stack_one.stack_data[_len: _len+1]:
            _len += 1
        return _len


if __name__ == '__main__':
    queue = MyQueue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.print_queue()
    queue.dequeue()
    queue.print_queue()
