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
    
    return self.data.pop()

  def stack_peek(self):
    if self.is_empty():
      return False
    
    return self.data[-1]

expression = "A+B*C/(E-F)"
reversed_exp = ""
stack = Stack([], len(expression))
operators = ['*', '/', '+', '-', '(', ')', '^']

for i in expression[::-1]:
  if i == '(':
    reversed_exp = reversed_exp + ')'
  elif i == ')':
    reversed_exp = reversed_exp + '('
  else:
    reversed_exp = reversed_exp + i


for i in reversed_exp:
  token = i
  # Verify if a token is in operator
  if token in operators:
    # if stack is empty then push operator to the stack
    if stack.is_empty():
      stack.stack_push(token)
    # if stack is not empty
    else:
      # verify if a token is multiplication or division
      if token == '*' or token == '/':
        # display and pop operators from the stack with higher or same level, after that, push the operator
        while stack.stack_peek() == '*' or stack.stack_peek() == '/' or stack.stack_peek() == '^':
          print(stack.stack_pop(), end='')
        stack.stack_push(token)
      
      #verify token if addition or subtraction
      elif token == '+' or token == '-':
        # display and pop operators from the stack with higher or same level, after that, push the operator
        while stack.stack_peek() == '+' or stack.stack_peek() == '-' or stack.stack_peek() == '*' or stack.stack_peek() == '/' or stack.stack_peek() == '^':
          print(stack.stack_pop(), end='')
        stack.stack_push(token)

      # verify if token is open parenthesis
      elif token == '(':
        # then push to the stack
        stack.stack_push(token)

      # verify token if close parenthesis
      elif token == ')':
        # while a peek is not reaching the open parenthesis
        while stack.stack_peek() != '(':
          # display and pop operators
          print(stack.stack_pop(), end='')
        # don't display the open parenthesis
        stack.stack_pop()

      # verify token if exponent
      elif token == '^':
        # while a peek is not reaching the exponent operator
        while stack.stack_peek() == '^':
          # display and pop operators with the higher or same level
          print(stack.stack_pop(), end='')
        # then push exponent operator
        stack.stack_push(token)
        
  else:
    # print immediately if not an operator
    print(token, end='')

# display operators left from the stack
for i in range(stack.length):
  if stack.is_empty(): break
  print(stack.stack_pop(), end='')