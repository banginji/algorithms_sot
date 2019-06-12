class BTNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def create_bt():
    node_minus_one = BTNode(-1)
    node_zero = BTNode(1)
    node_one = BTNode(1)
    node_two = BTNode(0)
    node_three = BTNode(3)
    node_four = BTNode(4)
    node_five = BTNode(5)
    node_six = BTNode(6)
    node_seven = BTNode(-6)
    node_eight = BTNode(6)
    node_nine = BTNode(0)

    node_six.left = node_two
    node_six.right = node_eight
    node_two.left = node_zero
    node_two.right = node_four
    node_zero.left = node_minus_one
    # node_zero.right = node_one
    node_four.left = node_three
    node_four.right = node_five
    node_eight.left = node_seven
    node_eight.right = node_nine

    return node_six


def num_paths(root, sum):
    idx_node = root
    nodes_order = []

    in_order_traversal(idx_node, nodes_order)

    num = 0

    for node in nodes_order:
        num+=num_paths_node(node, sum)

    return num


def num_paths_node(node, sum):
    num = 0

    if node.val == sum:
        num += 1
    if node.left==None or node.right==None:
        return num

    num+=num_paths_node(node.left, sum - node.val)
    num+=num_paths_node(node.right, sum - node.val)
    return num


def in_order_traversal(node, result):
    if not node:
        return

    in_order_traversal(node.left, result)
    result.append(node)
    in_order_traversal(node.right, result)


if __name__ == '__main__':
    print("Num Paths Impl")
    print(num_paths(create_bt(), 6))
