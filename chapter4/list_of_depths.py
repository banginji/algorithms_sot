from datastructures import LinkedList


class BinaryTreeNode:
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
    node_four.left_child = node_seven

    return root_node


def list_of_depths(children, result_list):
    if len(children) is 0:
        return
    same_depth_list = LinkedList.LinkedList_Single()
    for child in children:
        same_depth_list.add_node_to_list(child)
    result_list.append(same_depth_list)
    children_of_children = []
    current_node = same_depth_list.head
    while current_node is not None:
        if current_node.data.left_child is not None:
            children_of_children.append(current_node.data.left_child)
        if current_node.data.right_child is not None:
            children_of_children.append(current_node.data.right_child)
        current_node = current_node.next
    list_of_depths(children_of_children, result_list)


if __name__ == '__main__':
    root_node = create_binary_tree()
    result_list = []
    list_of_depths([root_node], result_list)
    for same_depth_nodes in result_list:
        same_depth_nodes.print_list()
