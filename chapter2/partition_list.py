from datastructures import  LinkedList as L


def partition_list(list, number):
    greater_than_number_list = L.LinkedList()
    lesser_than_number_list = L.LinkedList()
    current = list.head
    while current is not None:
        if current.data > number:
            greater_than_number_list.add(current.data)
        else:
            lesser_than_number_list.add(current.data)
        current = current.next
    lesser_than_number_list_tail = lesser_than_number_list.head
    while lesser_than_number_list_tail.next is not None:
        lesser_than_number_list_tail = lesser_than_number_list_tail.next
    lesser_than_number_list_tail.next = greater_than_number_list.head
    return lesser_than_number_list


if __name__ == '__main__':
    linked_list = L.LinkedList()
    linked_list.add_array_of_elements_to_list([34, 355, 124, 656, 123, 767, 34, 542, 123])
    partitioned_list = partition_list(linked_list, 125)
    partitioned_list.print_list()