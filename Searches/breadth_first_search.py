from tree import construct_tree, show_options

def breadth_first_search(root, goal):
  queue = [root]

  while queue:
    current_node = queue.pop(0)
    print(current_node.value)

    if current_node.value == goal:
      return True

    # Left 
    if current_node.left:
      queue.append(current_node.left)

    # Right
    if current_node.right:
      queue.append(current_node.right)
    
  return False

def start():
  root = construct_tree()

  show_options()
  goal = input("Please choose a location: ")

  print(f"\n==== Searching {goal} Using BFS ====")
  is_found = breadth_first_search(root, goal)
  print("=================================")

  if is_found:
    print(f"\nLocation '{goal}' found!")
  else:
    print("\nResult: All nodes have been traversed. The goal cannot be found.")


start()