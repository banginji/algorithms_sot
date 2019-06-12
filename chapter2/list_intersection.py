from datastructures import LinkedList


def is_intersecting(list_a, list_b):
    current_a = list_a.head
    current_b = list_b.head

    while current_a is not None:
        while current_b is not None:
            if current_a is current_b:
                return True
            current_b = current_b.next
        current_a = current_a.next
        current_b = list_b.head
    return False


if __name__ == '__main__':
    list_a = LinkedList.LinkedList_Single()
    list_b = LinkedList.LinkedList_Single()

    list_a.add_array_of_data_to_linked_list([1, 4, 5])
    list_b.add_array_of_data_to_linked_list([1, 12, 13, 14, 15])

    list_a.print_list()
    list_b.print_list()

    list_a.head.next.next = list_b.head.next.next.next

    list_a.print_list()
    list_b.print_list()

    print(is_intersecting(list_a, list_b))