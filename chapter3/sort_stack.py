from datastructures import stack


def sort_stack(stack_to_be_sorted):
    stack_buffer = stack.Stack()

    stack_buffer.push(stack_to_be_sorted.pop())

    while stack_to_be_sorted._len_stack() is not 0:
        temp = stack_to_be_sorted.pop()
        count = 0
        while stack_buffer.peek() > temp:
            stack_to_be_sorted.push(stack_buffer.pop())
            count += 1
        stack_buffer.push(temp)
        for i in range(count):
            stack_buffer.push(stack_to_be_sorted.pop())
    while stack_buffer._len_stack() is not 0:
        stack_to_be_sorted.push(stack_buffer.pop())


if __name__ == '__main__':
    stack_to_be_sorted = stack.Stack()
    stack_to_be_sorted.push(32)
    stack_to_be_sorted.push(12)
    stack_to_be_sorted.push(532)
    stack_to_be_sorted.push(1)
    stack_to_be_sorted.print_stack()
    sort_stack(stack_to_be_sorted)
    stack_to_be_sorted.print_stack()