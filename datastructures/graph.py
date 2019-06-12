class Graph:
    def __init__(self):
        self.nodes = []


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.children = []