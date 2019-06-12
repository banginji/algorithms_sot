class DoublyLinkedListNode:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next


class SingleLinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, data):
        node = DoublyLinkedListNode(data)
        current = self.head
        if self.head is None:
            self.head = node
        else:
            while current.next is not None:
                current = current.next
            current.next = node

    def print_list(self):
        current = self.head
        while current is not None:
            print(f"{current.data}", end=" -> ")
            current = current.next
        print(f"None")

    def add_array_of_elements_to_list(self, arr):
        if self.head is None:
            self.head = DoublyLinkedListNode(arr[0])
            current = self.head
        else:
            current = self.head
        while current.next is not None:
            current = current.next
        for i in range(1, len(arr)):
            current.next = DoublyLinkedListNode(arr[i], prev=current)
            current = current.next

    def remove_element_from_list(self, data):
        if self.head is None:
            return f"{data} not found in list"
        else:
            current = self.head
            while current.next is not None:
                if current.data == data:
                    current.prev.next = current.next
                    return f"Found and removed {data}"
                current = current.next
            return f"{data} not found in list"


def create_doubly_linked_list(arr):
    head = DoublyLinkedListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = DoublyLinkedListNode(arr[i], prev=current)
        current = current.next
    return head


def create_single_linked_list(arr):
    tail = SingleLinkedListNode(arr[len(arr)-1])
    current = tail
    for i in range(len(arr)-2, -1, -1):
        current = SingleLinkedListNode(arr[i], next=current)
    return current


class LinkedList_Single:

    def __init__(self):
        self.head = None

    def add_node_to_list(self, data):
        current = self.head
        if current is None:
            self.head = SingleLinkedListNode(data)
        else:
            while current.next is not None:
                current = current.next
            current.next = SingleLinkedListNode(data)

    def add_array_of_data_to_linked_list(self, arr):
        if len(arr)==0:
            return
        current = self.head
        if current is None:
            self.head = SingleLinkedListNode(arr[0])
            current = self.head
        else:
            while current.next is not None:
                current = current.next
            current.next = SingleLinkedListNode(arr[0])
            current = current.next
        for elem in arr[1:]:
            current.next = SingleLinkedListNode(elem)
            current = current.next

    def print_list(self):
        current = self.head
        while current is not None:
            print(f"{current.data}", end=" -> ")
            current = current.next
        print("None")

    def remove_node(self, data):
        current = self.head
        if current is None:
            print(f"{data} is not found in the list")
            return
        elif current.next is None:
            if current.data == data:
                self.head = None
                print(f"{data} was removed from list")
                return
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
            else:
                current = current.next
        if self.head.data == data:
            self.head = self.head.next

    def remove_tail(self):
        current = self.head
        if current is None:
            return
        elif current.next is None:
            self.head = None
            return
        while current.next.next is not None:
            current = current.next
        tail_node = current.next
        current.next = current.next.next
        return tail_node

    def seek_tail(self):
        current = self.head
        if self.head is None:
            return None
        elif self.head.next is None:
            return current
        else:
            while current.next is not None:
                current = current.next
        return current

    def add_node_to_head(self, data):
        if self.head is None:
            self.head = SingleLinkedListNode(data)
        else:
            new_node = SingleLinkedListNode(data)
            temp_head = self.head
            self.head = new_node
            self.head.next = temp_head
