class Node:
	def __init__(self, data=None, children=[]):
		self.data = data
		self.children = children

	def append_children(self, children=[]):
		self.children = children

	def traverse(self, parentNode, lvl):
		# POST ORDER
		for x in range(lvl):
			print('━━', end='')

		print(parentNode.data)

		for i in parentNode.children:
			self.traverse(i, lvl+1)

mark = Node("Mark Kenneth")
danessa = Node("Danessa Mae")
danilo = Node("Danilo")
gemma = Node("Gemma")
edith = Node("Edith")
ernie = Node("Ernie")
salvador = Node("Salvador")
czarina = Node("Czarina")
jhemart = Node("Jhemart")
justine = Node("Justine")
chariezse = Node("Chariezse Ashlee")
judyanne = Node("Judyanne")
leonardo = Node("Leonardo")
john = Node("John Matthew")
aileen = Node("Aileen Joy")
sky = Node("Skylerwin")

salvador.append_children([edith, danilo, gemma, ernie])
edith.append_children([judyanne, leonardo, john, aileen])
danilo.append_children([mark, danessa])
gemma.append_children([jhemart, justine, czarina])
ernie.append_children([chariezse, sky])

salvador.traverse(salvador, 0)