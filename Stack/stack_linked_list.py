class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

class StackLinkedList:
	def __init__(self, length=1):
		self.length = length
		self.peak = None
		self.base = None

	def is_full(self):
		current_node_count = 0
		current = self.base

		while (current != None):
			current = current.next
			current_node_count += 1
		
		if current_node_count >= self.length:
			return True
		
		return False
	
	def is_empty(self):
		if self.base == None:
			return True

		return False

	def get_peak(self):
		return self.peak

	def push(self, node):
		
		if self.is_full():
			print("Can't push to the stack. Stack is full.")
			return None

		if self.base == None:
			self.base = node
		else:
			self.peak.next = node

		self.peak = node
		return node.data

	def pop(self):

		if self.is_empty():
			return print("Nothing to pop. Stack is empty.")

		popped_data = None

		if self.base.next == None:
			popped_data = self.base
			self.base = None
			self.peak = None
			return popped_data
		
		current = self.base
		prev = None
		while (current.next != None):
			prev = current
			current = current.next

		popped_data = current
		prev.next = None
		self.peak = prev
		return popped_data

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
stack = StackLinkedList(3)
stack.push(node1)
stack.push(node2)
stack.push(node3)
stack.pop()

print("::: PRINTING DATA :::")
current = stack.base
while(current != None):
	print(current.data, end=', ')
	current = current.next