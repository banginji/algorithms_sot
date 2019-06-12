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


def in_order_traversal(node):
    if node is None:
        return
    in_order_traversal(node.left_child)
    print(f"{node.data}", end=", ")
    in_order_traversal(node.right_child)


def next_node(node, target_node_data, return_next_node):
    if node is None:
        return
    next_node(node.left_child, target_node_data, return_next_node)
    if return_next_node:
        print(node.data)
    if node.data is target_node_data:
        return_next_node = True
    next_node(node.right_child, target_node_data, return_next_node)


if __name__ == '__main__':
    root_node = create_binary_tree()
    next_node(root_node, 3, False)

