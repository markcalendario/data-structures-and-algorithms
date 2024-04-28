from tree import construct_tree, show_options

def depth_first_search(root, goal):
  stack = [root]

  while stack:
    current_node = stack.pop()
    print(current_node.value)

    if current_node.value == goal:
      return True

    # Right
    if current_node.right:
      stack.append(current_node.right)

    # Left 
    if current_node.left:
      stack.append(current_node.left)
    
  return False

def start():
  root = construct_tree()

  show_options()
  goal = input("Please choose a location: ")

  print(f"\n==== Searching {goal} Using DFS ====")
  is_found = depth_first_search(root, goal)
  print("=================================")

  if is_found:
    print(f"\nLocation '{goal}' found!")
  else:
    print("\nResult: All nodes have been traversed. The location cannot be found.")


start()