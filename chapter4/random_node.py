import random


class TreeNode():
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.size = 1

	def insert_node(self, val):
		if val < self.val:
			if self.left:
				self.left.insert_node(val)
			else:
				self.left = TreeNode(val)
		else:
			if self.right:
				self.right.insert_node(val)
			else:
				self.right = TreeNode(val)
		self.size += 1


	# Not complete Impl
	def random_node(self):
		random_idx = random.choice(range(self.size))
		left_size = 0
		if self.left:
			left_size = self.left.size
		if random_idx < left_size:
			self.left.random_node()
		elif random_idx == self.size:
			return self
		else:
			self.right.random_node()


def in_order_traversal(node):
	if not node:
		return
	in_order_traversal(node.left)
	print(node.val, end=", "+str(node.size)+"\n")
	in_order_traversal(node.right)


if __name__ == '__main__':
	print('Random Node Impl')
	root = TreeNode(3)
	for elem in [6, 1, -1, 4, 7, 0]:
		root.insert_node(elem)
	in_order_traversal(root)
	print(root.random_node().val, end="; Random Node")
