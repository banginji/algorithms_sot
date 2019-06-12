from datastructures import graph
import random
from collections import deque


def create_graph():
    start_node = graph.Node(0)
    node_1 = graph.Node(1)
    node_2 = graph.Node(2)
    node_3 = graph.Node(3)
    node_4 = graph.Node(4)
    node_5 = graph.Node(5)
    node_6 = graph.Node(6)

    start_node.children.append(node_1)
    node_1.children.append(node_2)
    node_2.children.append(start_node)
    node_2.children.append(node_3)
    node_3.children.append(node_2)

    node_3.children.append(node_5)

    node_4.children.append(node_6)
    node_5.children.append(node_4)
    node_6.children.append(node_5)

    start_graph = graph.Graph()
    start_graph.nodes.append(start_node)
    start_graph.nodes.append(node_1)
    start_graph.nodes.append(node_2)
    start_graph.nodes.append(node_3)
    start_graph.nodes.append(node_4)
    start_graph.nodes.append(node_5)
    start_graph.nodes.append(node_6)

    return start_graph


def is_there_path_between_nodes(node_one, node_two):
    traversible_nodes = deque([])
    traversible_nodes.append(node_one)

    while len(traversible_nodes) > 0:
        current_node = traversible_nodes.popleft()
        current_node.visited = True
        print(f"{current_node.name} -> ", end="")
        if current_node is node_two:
            return True
        for child in current_node.children:
            if not child.visited:
                traversible_nodes.append(child)
    return False


if __name__ == '__main__':
    start_graph = create_graph()
    start_node = random.choice(start_graph.nodes)
    end_node = random.choice(start_graph.nodes)
    while end_node is start_node:
        end_node = random.choice(start_graph.nodes)
    print(f"{start_node.name}, {end_node.name}")
    print(f"{is_there_path_between_nodes(node_one=start_node, node_two=end_node)}")