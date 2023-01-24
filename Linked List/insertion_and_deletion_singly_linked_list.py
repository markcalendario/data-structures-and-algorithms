class Node():
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

class LinkedList():
  def __init__(self):
    self.head = None
    self.tail = None

  def insert_to_beginning(self, new_node):
    # This function connects the current head to the next of new_node,
    # Then, it set the new_node as head
    if self.head != None:
      new_node.next = self.head
      self.head = new_node

  def insert_to_last(self, new_node):
    # This function connects the tail to the new_node and set the new_node as a new tail
    if self.tail != None:
      self.tail.next = new_node
      self.tail = new_node

  def insert_to_pos(self, new_node, pos, list_len):
    # This function inserts a new_node into a defined position (pos)
    # It traverse from the start of the linked list to the end
    # If the traversal is currently in the defined position, 
    # Then set the next of new_node to the next node of current node
    # Then connect the chain of the next of the current into new_node
    # It will cut the connection of A->B (magiging A B nalang, wala na yung connection)
    # Then, A->N->B (tapos, icoconnect na pati yung bago)
    current = self.head
    for i in range(list_len):
      if i == pos - 2:
        new_node.next = current.next
        current.next = new_node
        break
      current = current.next  

  def display_list(self):
    # Displays all the nodes
    print("\nListing all the data of the linked list: ")
    current = self.head
    while current != None:
      print("[" + current.data + "]" + " -> ", end="")
      current = current.next

  def delete_head(self):
    # It set the next node of head as a head
    self.head = self.head.next

  def delete_tail(self):
    # Traverses through the list until reaches the end
    # If the traversal is on the node that is second to the last
    # Then, set that node as a tail
    # Finally, remove the chain of the new tail (set as None)
    current = self.head
    while current != None:
      if current.next.next == None:
        self.tail = current
        self.tail.next = None
        break
      current = current.next

  def delete_pos(self, pos, list_len):
    # Traverses through the list until reaches the end
    # If the traversal is in the current position, then connect the link of current node to the next of next current node
    # A->B->C
    # A->C
    current = self.head
    for i in range(list_len):
      if i == pos - 2:
        current.next = current.next.next 
        break
      current = current.next

def insert_node(list, list_len):
  data = input("Enter data for this new node: ")
  new_node = Node(data)
  pos = 0
  
  while True:
    pos = int(input("Insert a position you want to insert a node: "))
    if pos > list_len + 1 or pos < 1:
      print("Out of bounds! 1 to " + str(list_len + 1) + " only.")
    else:
      break
  
  if pos == 1:
    list.insert_to_beginning(new_node)
  elif pos == list_len + 1:
    list.insert_to_last(new_node)
  else:
    list.insert_to_pos(new_node, pos, list_len)
  list.display_list()

def delete_node(list, list_len):
  pos = 0
  
  while True:
    pos = int(input("Enter a node position you want to delete: "))
    if pos > list_len or pos < 1:
      print("Out of bounds! 1 to " + str(list_len) + " only.")
    else:
      break
  
  if pos == 1:
    list.delete_head()
  elif pos == list_len:
    list.delete_tail()
  else:
    list.delete_pos(pos, list_len)
    
  list.display_list()

def start():
  # Initialize a linked list
  list = LinkedList()
  # Get number of nodes
  list_len = int(input("Enter number of nodes do you want to create: "))

  # Get data for each node
  for i in range(list_len):
    # Get data
    data = input("Enter data for node " + str(i + 1) + ": ")
    # Create a temporary node
    current = Node(data)
    
    
    if i == 0: # If temporary node is the first node of the list, then set as head
      list.head = current
    else: # otherwise, connect the current tail to temporary node
      list.tail.next = current
    
    # Set that temporary node as tail
    list.tail = current

  # Display all list
  list.display_list()

  # Menu
  print("\n\nMenu:")
  print("[A] Insert new node: ")
  print("[B] Delete a node: ")
  option = input("Enter an operation: ")

  if option == 'A' or option == 'a':
    insert_node(list, list_len) # Insert node
  else:
    delete_node(list, list_len) # Delete Node

start()