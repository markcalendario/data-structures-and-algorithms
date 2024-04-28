from tree import construct_tree

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
  goal = input("Please enter a goal: ")
  is_found = breadth_first_search(root, goal)

  if is_found:
    print(f"Goal {goal} found!")
  else:
    print("All nodes has been traversed. The goal cannot be found.")


start()