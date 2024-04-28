class Node:
  def assign_left(self, Node):
    self.left = Node

  def assign_right(self, Node):
    self.right = Node

  def __init__(self, value, distance):
    self.value = value
    self.distance = distance
    self.left = None
    self.right = None

def construct_tree_with_cost():
  root = Node("Gate", 0)

  gym = Node("Gym", 30)
  oval = Node("Oval", 40)
  pool = Node("Pool", 35)
  
  catwalk = Node("Catwalk", 10)
  souvenir_shop = Node("Souvenir Shop", 25)
  tennis_court = Node("Tennis Court", 30)

  root.assign_left(gym)
  root.assign_right(catwalk)

  gym.assign_left(oval)
  gym.assign_right(pool)

  catwalk.assign_left(souvenir_shop)
  catwalk.assign_right(tennis_court)

  return root

