import sys


class BinaryTreeNode():
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def create_binary_tree():
    root_node = BinaryTreeNode(5)
    node_one = BinaryTreeNode(3)
    node_two = BinaryTreeNode(7)
    node_three = BinaryTreeNode(2)
    node_four = BinaryTreeNode(4)
    node_five = BinaryTreeNode(6)
    node_six = BinaryTreeNode(8)
    node_seven = BinaryTreeNode(1)
    node_eight = BinaryTreeNode(1.5)

    root_node.left_child = node_one
    root_node.right_child = node_two
    node_one.left_child = node_three
    node_one.right_child = node_four
    node_two.left_child = node_five
    node_two.right_child = node_six
    node_three.left_child = node_seven
    node_seven.right_child = node_eight

    return root_node


def in_order_traversal(node, result_arr):
    if node is None:
        return
    in_order_traversal(node.left_child, result_arr)
    result_arr.append(node.data)
    in_order_traversal(node.right_child, result_arr)


def is_bst(node, _min, _max):
    if node is None:
        return True
    if node.data < _min or node.data > _max:
        return False
    return is_bst(node.left_child, _min, node.data) and is_bst(node.right_child, node.data, _max)


if __name__ == '__main__':
    root_node = create_binary_tree()

    result_list = []
    in_order_traversal(root_node, result_list)
    sorted_list = sorted(result_list)
    result = True
    for i, j in zip(result_list, sorted_list):
        if i != j:
            result = False
            break
        result = result and (i is j)
    print(result)
    print(is_bst(root_node, -sys.maxsize, sys.maxsize))
