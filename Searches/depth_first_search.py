from tree import construct_tree

def depth_first_search(root, goal):
  queue = [root]

  while queue:
    current_node = queue.pop()
    print(current_node.value)

    if current_node.value == goal:
      return True

    # Right
    if current_node.right:
      queue.append(current_node.right)

    # Left 
    if current_node.left:
      queue.append(current_node.left)
    
  return False

def start():
  root = construct_tree()
  goal = input("Please enter a goal: ")
  is_found = depth_first_search(root, goal)

  if is_found:
    print(f"Goal {goal} found!")
  else:
    print("All nodes has been traversed. The goal cannot be found.")


start()