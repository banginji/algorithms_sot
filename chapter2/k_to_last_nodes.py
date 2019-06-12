from datastructures import LinkedList as L


def list_k_end(list, start):
    index = 0
    current = list.head
    while True:
        if index == start:
            return current
        else:
            current = current.next
            index += 1


if __name__ == '__main__':
    linked_list = L.LinkedList()
    linked_list.add_array_of_elements_to_list([1, 2, 3, 4, 5, 6, 7])
    result = list_k_end(linked_list, 3)
    while result is not None:
        print(f"{result.data}", end=" -> ")
        result = result.next
    print("None")