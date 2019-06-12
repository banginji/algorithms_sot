from datastructures import LinkedList as L


def remove_k_node(list, k):
    current = list.head
    for idx in range(1, k+1):
        print(idx, end=", ")
        current = current.next
    current.next = current.next.next


if __name__ == '__main__':
    linked_list = L.LinkedList()
    linked_list.add_array_of_elements_to_list([34, 321, 124, 3251, 46, 34, 64, 234])
    remove_k_node(linked_list, 3)
    current = linked_list.head
    while current is not None:
        print(f"{current.data}", end=" -> ")
        current = current.next
    print("None")
