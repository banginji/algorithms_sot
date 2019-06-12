class BTNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


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
    node_zero.left = node_minus_one
    node_zero.right = node_one
    node_four.left = node_three
    node_four.right = node_five
    node_eight.left = node_seven
    node_eight.right = node_nine

    return (node_six, node_minus_one, node_seven)


def common_ancestor(root, p, q):
    ancestor = root

    def itx(node_itx, p, q):
        p_on_left = dfs(node_itx.left, p)
        q_on_left = dfs(node_itx.left, q)
        if p_on_left != q_on_left:
            return node_itx.val
        if p_on_left:
            return itx(node_itx.left, p, q)
        else:
            return itx(node_itx.right, p, q)

    def dfs(node_itx, search_node):
        if not node_itx:
            return False
        if node_itx == search_node:
            return True
        return dfs(node_itx.left, search_node) | dfs(node_itx.right, search_node)

    return itx(ancestor, p, q)


if __name__ == '__main__':
    print('Common Ancestor Impl')
    root, node_one, node_two = create_bt()
    print(common_ancestor(root, node_one, node_two))
