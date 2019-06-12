from datastructures import LinkedList as L


def remove_duplicates_from_list(list):
    data_list = []
    current = list.head
    while current.next is not None:
        if current.next.data in data_list:
            current.next = current.next.next
        else:
            data_list.append(current.data)
            current = current.next
    if list.head.data in data_list:
        list.head = list.head.next


def remove_duplicates_without_buffer(list):
    current = L.SingleLinkedListNode("")
    current.next = list.head
    while current.next is not None:
        inner_current = current.next
        while inner_current.next is not None:
            if current.next.data == inner_current.next.data:
                inner_current.next = inner_current.next.next
            else:
                inner_current = inner_current.next
        current = current.next


if __name__ == '__main__':
    linked_list = L.LinkedList()
    linked_list.add_array_of_elements_to_list([34, 1, 2, 1, 4, 5, 34, 6, 7, 34])
    linked_list.print_list()
    linked_list.add(23)
    linked_list.print_list()
    linked_list.remove_element_from_list(4)
    linked_list.print_list()
    remove_duplicates_without_buffer(linked_list)
    linked_list.print_list()

    single_linked_list = L.LinkedList_Single()
    single_linked_list.add_array_of_data_to_linked_list([1, 1, 1, 1])
    single_linked_list.print_list()
    single_linked_list.add_array_of_data_to_linked_list([1, 1, 1, 1, 1])
    single_linked_list.print_list()
    # single_linked_list.remove_node(1)
    remove_duplicates_without_buffer(single_linked_list)
    single_linked_list.print_list()
    print(end="\n")
