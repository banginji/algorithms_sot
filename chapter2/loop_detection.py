from datastructures import LinkedList


def is_looped(list):
    current = list.head
    traversed_nodes = []
    traversed_nodes.append(current)

    while current.next is not None:
        current = current.next
        if current in traversed_nodes:
            return True
        traversed_nodes.append(current)

    return False


if __name__ == '__main__':
    list_a = LinkedList.LinkedList_Single()
    list_a.add_array_of_data_to_linked_list([1, 2, 3, 4, 5, 6, 7])

    list_a.print_list()
    # list_a.seek_tail().next = list_a.head.next.next

    print(is_looped(list_a))
