class Leaf():
  def __init__(self, val=0):
    self.val = val
    self.right = None
    self.left = None
    self.visited = False

class BinaryTree():
  def __init__(self, root):
    self.root = root

  def print_in_order(self, node, traversal):
    #traversal = ""
    if node != None:
      traversal = self.print_in_order(node.left, traversal)
      traversal += str(node.val)
      traversal = self.print_in_order(node.right, traversal)

    return traversal

  def pre_order(self, node, traversal):
    #traversal = ""
    if node != None:
      traversal += str(node.val)
      #print(traversal)
      traversal = self.pre_order(node.left, traversal)
      traversal = self.pre_order(node.right, traversal)

    return traversal

  def post_order(self, node, traversal):
    #traversal = ""
    if node != None:
      traversal = self.post_order(node.left, traversal)
      traversal = self.post_order(node.right, traversal)
      traversal += str(node.val)
      #print(traversal)
    return traversal


  def visit_node(self, node):
    print(node.val)

class MinHeap():
  def __init__(self, root):
    self.root = root


  def add_element(self, item):
      # Add to the bottom+rightmost position,
      # check with parent and keep swapping
    pass

  def remove_element(self, item):
    # Look for element
    # Remove element and swap with bottom-most element
    # Then heapify
    pass

  def find_element(self, root, item):
    if root == None:
      return False
    if root.val == item:
      return True
    else:
      return(self.find_element(root.left, item) or
      self.find_element(root.right, item))
    pass

  def get_min(self):
    mini = self.root.val
    return mini

root = Leaf(0)
root.left = Leaf(1)
root.right = Leaf(2)
root.left.left = Leaf(3)
root.left.right = Leaf(4)
root.right.left = Leaf(5)
root.right.right = Leaf(6)

traversal = ""
bt = BinaryTree(root)

#traversal = bt.print_in_order(root, traversal)
#traversal = bt.pre_order(root, traversal)
#traversal = bt.post_order(root, traversal)
print(traversal)