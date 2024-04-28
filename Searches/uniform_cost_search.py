from tree_with_cost import construct_tree_with_cost, show_options

def uniform_cost_search(root, goal):
  frontier = [[root.distance, root, root.distance]]
  visited = []

  while frontier:
    # Sort the frontier based on the cost (distance)
    frontier.sort(key=lambda x: x[0])
    # Pop the node with the lowest cost
    current_distance, current_node, total_cost = frontier.pop(0)
    
    # Print the current node's value and total cost
    print("Visiting:", current_node.value, "with total cost:", total_cost)
    
    # Check if the goal state has reached
    if current_node.value == goal:
      return True, total_cost
    
    # Add the current node to visited list
    visited.append(current_node)
      
    # Combine the current distance and the distance of left node
    if current_node.left and current_node.left not in visited:
      child_distance = current_distance + current_node.left.distance
      frontier.append((child_distance, current_node.left, child_distance))

    # Combine the current distance and the distance of right node
    if current_node.right and current_node.right not in visited:
      child_distance = current_distance + current_node.right.distance
      frontier.append((child_distance, current_node.right, child_distance))

  return False, None

def start():
  root = construct_tree_with_cost()

  show_options()
  goal = input("Please choose a location: ")

  print(f"\n==== Searching {goal} Using UCS ====")
  is_found, cost = uniform_cost_search(root, goal)
  print("=================================")

  if is_found:
    print(f"\nLocation {goal} found with the distance of {cost} meters.")
  else:
    print("\nAll nodes have been traversed. The location cannot be found.")



 

start()