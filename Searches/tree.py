class Node:
  left: None
  right: None
  value: None

  def assign_left(self, Node):
    self.left = Node

  def assign_right(self, Node):
    self.right = Node

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def construct_tree():
  root = Node("Gate")

  gym = Node("Gym")
  oval = Node("Oval")
  pool = Node("Pool")
  
  catwalk = Node("Catwalk")
  souvenir_shop = Node("Souvenir Shop")
  tennis_court = Node("Tennis Court")

  root.assign_left(gym)
  root.assign_right(catwalk)

  gym.assign_left(oval)
  gym.assign_right(pool)

  catwalk.assign_left(souvenir_shop)
  catwalk.assign_right(tennis_court)

  return root
