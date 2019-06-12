import random


class StackThreeInOne:
    def __init__(self, stack_size, number_of_stacks):
        self.stack_data = [0 for _ in range(stack_size)] * number_of_stacks
        # self.top_end = [(0, -1, 2), (3, 2, 5), (6, 5, 8)]
        self.top_end = []
        for stack_idx in range(number_of_stacks):
            stack_top = stack_idx * stack_size
            stack_first_element = stack_top - 1
            stack_end = stack_first_element + stack_size
            self.top_end.append((stack_top, stack_first_element, stack_end))
        self.number_of_stacks = number_of_stacks

    def push(self, data, stack_idx):
        # random_idx = self.__random_stack_index()
        selected_top, selected_first, selected_end = self.top_end[stack_idx]

        if selected_first is selected_end:
            return

        idx = selected_first
        while idx >= selected_top:
            self.stack_data[idx+1] = self.stack_data[idx]
            idx -= 1

        self.stack_data[selected_top] = data

        selected_first += 1
        self.top_end[stack_idx] = selected_top, selected_first, selected_end

    def pop(self, stack_idx):
        # random_idx = self.__random_stack_index()
        selected_top, selected_first, selected_end = self.top_end[stack_idx]

        if selected_first is selected_top-1:
            return

        return_data = self.stack_data[selected_top]

        idx = selected_top
        while idx < selected_first:
            self.stack_data[idx] = self.stack_data[idx+1]
            idx += 1

        self.stack_data[selected_first] = 0

        selected_first -= 1
        self.top_end[stack_idx] = selected_top, selected_first, selected_end

        return return_data

    def __random_stack_index(self):
        return random.choice(range(len_list(self.top_end)))

    def print_stack(self):
        # len = len_list(self.stack_data)
        for stack_idx in range(self.number_of_stacks):
            selected_top, _, selected_end = self.top_end[stack_idx]
            print("[", end="")
            idx = selected_top
            while idx <= selected_end:
                print(f"{self.stack_data[idx]}", end=", ")
                idx += 1
            print("], ", end="")

def len_list(list):
    len = 0
    while list[len: len+1]:
        len += 1
    return len


if __name__ == '__main__':
    stack = StackThreeInOne(5, 3)
    stack.push(10, 0)
    stack.push(20, 2)
    stack.push(30, 1)
    stack.push(40, 2)
    stack.push(50, 1)
    stack.push(60, 0)
    stack.push(70, 1)
    stack.push(80, 2)
    stack.push(90, 0)
    stack.push(100, 1)
    stack.push(110, 1)
    stack.print_stack()
    print("\n")
    print(stack.pop(1))
    print(stack.pop(1))
    print(stack.pop(0))
    print(stack.pop(0))
    print(stack.pop(0))
    print(stack.pop(2))
    print(stack.pop(0))
    print(stack.pop(1))
    print(stack.pop(1))
    print("\n")
    stack.print_stack()
