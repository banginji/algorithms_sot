class PlatOfStacks:
    def __init__(self):
        self.stacks = []
        self.present_stack_index = -1
        self.individual_stack_size = 5

    def push(self, data):
        if self.__len_stack__(self.stacks) is 0:
            self.__add_stack__()
        if self.__len_stack__(self.stacks[self.present_stack_index]) is self.individual_stack_size:
            self.__add_stack__()
        self.stacks[self.present_stack_index] = [data] + self.stacks[self.present_stack_index]

    def pop(self):
        if self.__len_stack__(self.stacks[self.present_stack_index]) is 0:
            self.__remove_stack__()
        if self.__len_stack__(self.stacks) is 0:
            return
        self.stacks[self.present_stack_index] = self.stacks[self.present_stack_index][1:]

    def __len_stack__(self, _stack):
        _len = 0
        while _stack[_len: _len+1]:
            _len += 1
        return _len

    def __add_stack__(self):
        self.stacks.append([])
        self.present_stack_index += 1

    def __remove_stack__(self):
        self.stacks = self.stacks[:self.present_stack_index]
        self.present_stack_index -= 1

    def print_stack(self):
        for stack_idx in range(self.__len_stack__(self.stacks)):
            print("[", end="")
            for idx in range(self.__len_stack__(self.stacks[stack_idx])):
                print(f"{self.stacks[stack_idx][idx]}", end=", ")
            print("], ", end="")

    def pop_from_stack(self, stack_idx):
        if stack_idx > self.present_stack_index:
            print(f"Stack not yet populated")
            return
        idx = stack_idx
        self.stacks[idx] = self.stacks[idx][1:]
        while idx < self.present_stack_index:
            self.stacks[idx] = [self.stacks[idx+1][4]] + self.stacks[idx]
            self.stacks[idx+1] = self.stacks[idx+1][:4]
            idx += 1
        self.stacks[self.present_stack_index] = self.stacks[self.present_stack_index][:4]


if __name__ == '__main__':
    stack = PlatOfStacks()
    for i in range(0, 200, 10):
        stack.push(i)
    stack.print_stack()
    print(end="\n")
    for i in range(21):
        stack.pop()
    stack.print_stack()

    stack_new = PlatOfStacks()
    for i in range(0, 200, 10):
        stack_new.push(i)
    stack_new.print_stack()
    print(end="\n")
    stack_new.pop_from_stack(1)
    stack_new.print_stack()