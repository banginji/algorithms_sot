class BinaryTreeNode():
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def create_binary_tree():
    root_node = BinaryTreeNode(0)
    node_one = BinaryTreeNode(1)
    node_two = BinaryTreeNode(2)
    node_three = BinaryTreeNode(3)
    node_four = BinaryTreeNode(4)
    node_five = BinaryTreeNode(5)
    node_six = BinaryTreeNode(6)
    node_seven = BinaryTreeNode(7)

    root_node.left_child = node_one
    root_node.right_child = node_two
    node_one.left_child = node_three
    node_one.right_child = node_four
    node_two.left_child = node_five
    node_two.right_child = node_six
    node_three.left_child = node_seven

    return root_node


def is_tree_balanced(root):
    return abs(height_node(root.left_child) - height_node(root.right_child)) < 1


def height_node(node):
    lh = -1
    rh = -1

    if node.left_child is not None:
        lh += height_node(node.left_child)
        lh += 1
    else:
        lh += 1

    if node.right_child is not None:
        rh += height_node(node.right_child)
        rh += 1
    else:
        rh += 1

    return max(lh, rh)


if __name__ == '__main__':
    root_node = create_binary_tree()
    print(is_tree_balanced(root_node))