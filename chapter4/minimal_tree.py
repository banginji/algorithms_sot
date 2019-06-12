class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None


def create_left_right_nodes(arr, node):
    if len(arr) <= 1:
        return
    left_arr = arr[:len(arr) // 2]
    node.left_node = BinarySearchTreeNode(left_arr[len(left_arr) // 2])
    create_left_right_nodes(left_arr, node.left_node)

    if len(arr) > 2:
        right_arr = arr[len(arr) // 2 + 1:]
        node.right_node = BinarySearchTreeNode(right_arr[len(right_arr) // 2])
        create_left_right_nodes(right_arr, node.right_node)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    root_node = BinarySearchTreeNode(arr[len(arr) // 2])
    create_left_right_nodes(arr, root_node)
    print("")
