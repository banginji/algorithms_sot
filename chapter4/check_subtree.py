class BTNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def create_bt1():
    node_minus_one = BTNode(-1)
    node_zero = BTNode(0)
    node_one = BTNode(1)
    node_two = BTNode(2)
    node_three = BTNode(3)
    node_four = BTNode(4)
    node_five = BTNode(5)
    node_six = BTNode(6)
    node_seven = BTNode(7)
    node_eight = BTNode(8)
    node_nine = BTNode(9)

    node_six.left = node_two
    node_six.right = node_eight
    node_two.left = node_zero
    node_two.right = node_four
    node_zero.left = node_minus_one
    node_zero.right = node_one
    node_four.left = node_three
    node_four.right = node_five
    node_eight.left = node_seven
    node_eight.right = node_nine

    return node_six


def create_bt2():
    node_minus_one = BTNode(-1)
    node_zero = BTNode(0)
    node_one = BTNode(1)
    node_two = BTNode(2)
    node_three = BTNode(3)
    node_four = BTNode(4)
    node_five = BTNode(5)

    node_two.left = node_zero
    node_two.right = node_four
    node_zero.left = node_minus_one
    node_zero.right = node_one
    node_four.left = node_three
    node_four.right = node_five

    return node_two


def check_subtree(root1, root2):
    result1, result2 = [], []
    pre_order_traversal(root1, result1)
    pre_order_traversal(root2, result2)
    return set(result2) - set(result1) == set()


def pre_order_traversal(node, result):
    if not node:
        return
    result.append(node.val)
    pre_order_traversal(node.left, result)
    pre_order_traversal(node.right, result)


if __name__ == '__main__':
    print('Check Subtree Impl')
    root1, root2 = create_bt1(), create_bt2()
    print(check_subtree(root1, root2))
