from datastructures import LinkedList


def is_palindrome(list):
    tail = list.seek_tail()

    while list.head is not None:
        if list.head.next is None:
            return True
        else:
            if list.head.data is not tail.data:
                return False
            else:
                list.head = list.head.next
                list.remove_tail()
                tail = list.seek_tail()
    return True

if __name__ == '__main__':
    palindrome_string = "tuvdnggndvut"
    list = LinkedList.LinkedList_Single()
    list.add_array_of_data_to_linked_list(palindrome_string)
    print(is_palindrome(list))