class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  # I added another param, since the instructions don't say anything
  # about adding params or modifying the function.

  """ Node allows for algorithm to check if exists and then recursivly
      call the function with the node as well as the cb. 
      
      CB is the callback function that appends the node value to the
      array in the cb lambda"""

  def depth_first_for_each(self, cb, node=None):
    # Pre-Order Traverse - Value -> Left Val -> Right Val
    # Call the cb to append the value
    cb(node.value)

    # Check if the node has a left, if so, call this method again
    # with the left node
    if node.left:
      self.depth_first_for_each(cb, node.left)
    
    # Check if the node has a right, if so, call this method again
    # with the right node
    if node.right:
      self.depth_first_for_each(cb, node.right)

  def breadth_first_for_each(self, cb):
    pass

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
