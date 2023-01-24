class Stack:
  def __init__(self, data=[], length=0):
    self.length = length
    self.data = data

  def is_full(self):
    if len(self.data) == self.length:
      return True

    return False

  def is_empty(self):
    if len(self.data) == 0:
      return True
    
    return False

  def stack_push(self, item):
    if self.is_full():
      print("Stack is full, you cannot enter an item to a stack.")
      return False

    self.data.append(item)

  def stack_pop(self):
    if self.is_empty():
      print("Stack is empty, you cannot pop an item from a stack.")
      return False

    self.data.pop()

  def stack_peek(self):
    if self.is_empty():
      print("Stack is empty, unable to find a top of a stack.")
      return False
    
    return self.data[-1]

stack = Stack([], 50)
stack.stack_push('a')
stack.stack_push('b')
stack.stack_push('c')
stack.stack_push('d')
stack.stack_push('e')
stack.stack_push('f')
print(stack.data)