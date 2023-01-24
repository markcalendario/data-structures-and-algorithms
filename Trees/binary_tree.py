class Node:
	def __init__(self, data=None, left=None, right=None):
		self.data = data
		self.left = left
		self.right = right

	def assign_left(self, node):
		self.left = node
  
	def assign_right(self, node):
		self.right = node

class Tree:
	root = None

#####################################

root = Node("Root")

parentLeft = Node("Parent A")
rightChildA = Node("Right Child of Parent A")
leftChildA = Node("Left Child of Parent B")

parentRight = Node("Parent B")
rightChildB = Node("Right Child of B")
leftChildB = Node("Left Child of B")

root.assign_left(parentLeft)
parentLeft.assign_left(leftChildA)
parentLeft.assign_right(rightChildA)

root.assign_right(parentRight)
parentRight.assign_left(leftChildB)
parentRight.assign_left(rightChildB)


print(root.left.right.data)