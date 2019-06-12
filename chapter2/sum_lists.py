from datastructures import LinkedList


def sum_lists_backward(list_a, list_b):
    current_a = list_a.head
    current_b = list_b.head

    # sum = []
    sum = LinkedList.LinkedList_Single()
    carry = 0

    while current_a is not None or current_b is not None:
        if current_a is None:
            temp_sum = current_b.data + carry
        elif current_b is None:
            temp_sum = current_a.data + carry
        else:
            temp_sum = current_a.data + current_b.data + carry

        if temp_sum > 9:
            # sum.append(temp_sum%10)
            sum.add_node_to_list(temp_sum%10)
            carry = 1
        else:
            # sum.append(temp_sum)
            sum.add_node_to_list(temp_sum)
            carry = 0

        if current_a:
            current_a = current_a.next
        if current_b:
            current_b = current_b.next

    if carry != 0:
        # sum.append(carry)
        sum.add_node_to_list(carry)

    return sum


def sum_lists_forward(list_a, list_b):
    tail_a = list_a.seek_tail()
    tail_b = list_b.seek_tail()

    sum_list = LinkedList.LinkedList_Single()
    carry = 0

    while tail_a is not None or tail_b is not None:
        if tail_a is None:
            temp_sum = tail_b.data + carry
        elif tail_b is None:
            temp_sum = tail_a.data + carry
        else:
            temp_sum = tail_a.data + tail_b.data + carry
        if temp_sum > 9:
            sum_list.add_node_to_head(temp_sum%10)
            carry = 1
        else:
            sum_list.add_node_to_head(temp_sum)
            carry = 0
        list_a.remove_tail()
        list_b.remove_tail()
        tail_a = list_a.seek_tail()
        tail_b = list_b.seek_tail()

    if carry != 0:
        sum_list.add_node_to_head(carry)
    return sum_list


if __name__ == '__main__':
    list_a = LinkedList.LinkedList_Single()
    list_a.add_array_of_data_to_linked_list([5, 6, 7, 3, 4, 9, 9])

    list_b = LinkedList.LinkedList_Single()
    list_b.add_array_of_data_to_linked_list([9, 9, 9])

    sum_list = sum_lists_forward(list_a, list_b)
    sum_list.print_list()

