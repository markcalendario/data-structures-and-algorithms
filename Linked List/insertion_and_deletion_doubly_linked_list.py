class Node:
  def __init__(self, data = None, next = None, prev = None):
    self.data = data
    self.next = next
    self.prev = prev

class DoublyLinkedList:
  def __init__(self, head = None, tail = None):
    self.head = head
    self.tail = tail

  def insert_to_beginning(self, new_node):
    new_node.next = self.head
    self.head.prev = new_node
    self.head = new_node

  def insert_to_last(self, new_node):
    new_node.prev = self.tail
    self.tail.next = new_node
    self.tail = new_node

  def insert_to_pos(self, new_node, pos, linklist_len):
    current = self.head
    for i in range(1, linklist_len):
      if i == pos - 1:
        new_node.prev = current
        new_node.next = current.next
        current.next.prev = new_node
        current.next = new_node
        break
      current = current.next

  def delete_beginning(self):
    self.head = self.head.next
    self.head.prev = None

  def delete_last(self):
    self.tail = self.tail.prev
    self.tail.next = None

  def delete_pos(self, pos, linklist_len):
    current = self.head
    for i in range(1, linklist_len + 1):
      if i == pos - 1:
        current.next = current.next.next
        current.next.prev = current
        break
      current = current.next

  def display_linklist(self):
    print("\nDisplaying Forward:")
    current = self.head

    while current != None:
      print("[" + current.data + "] -> ", end="")
      current = current.next
    
    current = self.tail
    print("\nDisplaying Backwards:")
    while current != None:
      print("[" + current.data + "] -> ", end="")
      current = current.prev

def insert_node(list, linklist_len):
  data = input("Enter a data for new node: ")
  new_node = Node(data)
  pos = 0
  
  while True:
    try:
      pos = int(input(f"Enter position you want to enter this node [1-{linklist_len} ({linklist_len + 1} for last)]: "))
      if pos > linklist_len + 1 or pos < 1:
        print("Out of bounds position.")
      else:
        break
    except:
      print("Bad input.")
      
  if pos == 1:
    list.insert_to_beginning(new_node)
  elif pos == linklist_len + 1:
    list.insert_to_last(new_node)
  else:
    list.insert_to_pos(new_node, pos, linklist_len)

def delete_node(list, linklist_len):
  pos = int(input("Enter node position you want to delete [1-5]: "))
  
  if pos == 1:
    list.delete_beginning()
  elif pos == linklist_len:
    list.delete_last()
  else:
    list.delete_pos(pos, linklist_len)

def start():
  list = DoublyLinkedList()
  linklist_len = 5

  for i in range(1, linklist_len + 1):
    data = input("Enter data for node " + str(i) + ": ")
    current = Node(data)

    if i == 1:
      list.head = current
    else:
      list.tail.next = current
      current.prev = list.tail

    list.tail = current

  print("\nMenu:")
  print("[A] Insert a new node")
  print("[B] Delete a node")
  operation = input("Enter an operation: ")

  if operation == 'A' or operation == 'a':
    insert_node(list, linklist_len)
  else:
    delete_node(list, linklist_len)

  list.display_linklist()

start()