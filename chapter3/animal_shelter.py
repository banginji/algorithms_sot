from chapter3 import my_queue
import random


def random_name():
    return ''.join(random.choice('0123456789ABCDE') for _ in range(5))


def first_animal_in_line(queue1, queue2):
    _, queue1_number = queue1.stack_one.stack_data[queue1._len_queue()-1]
    _, queue2_number = queue2.stack_one.stack_data[queue2._len_queue()-1]
    if queue1_number < queue2_number:
        return queue1.stack_one.stack_data[queue1._len_queue()-1]
    else:
        return queue2.stack_one.stack_data[queue2._len_queue()-1]


if __name__ == '__main__':
    dog_queue = my_queue.MyQueue()
    cat_queue = my_queue.MyQueue()

    queue_number = 0

    for i in range(10):
        current_queue = random.choice((dog_queue, cat_queue))
        current_queue.enqueue((random_name(), queue_number))
        queue_number += 1

    dog_queue.print_queue()
    cat_queue.print_queue()
    print(first_animal_in_line(dog_queue, cat_queue))
