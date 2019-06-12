class BTNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def create_bt():
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
    node_two.parent = node_six
    node_zero.left = node_minus_one
    node_zero.right = node_one
    node_zero.parent = node_two
    node_four.left = node_three
    node_four.right = node_five
    node_four.parent = node_two
    node_eight.left = node_seven
    node_eight.right = node_nine
    node_eight.parent = node_six
    node_minus_one.parent = node_zero
    node_one.parent = node_zero
    node_three.parent = node_four
    node_five.parent = node_four
    node_seven.parent = node_eight
    node_nine.parent = node_eight

    return node_nine


def successor(node):
    if node.right:
        itx = node.right
        while itx.left:
            itx = itx.left
        return itx
    else:
        itx = node
        parent = node.parent
        while parent != None and itx != parent.left:
            itx = parent
            parent = parent.parent
        return parent


if __name__ == '__main__':
    print('BST Successor Impl')
    target_node = create_bt()
    successor = successor(target_node)
    if successor:
        print(successor.val)
    else:
        print('None')
