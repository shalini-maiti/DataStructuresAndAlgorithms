class Node:
  def __init__(self, data=0):
    self.data = data
    self.next = None
    pass

class LinkedList:
  def __init__(self, root):
    self.root = root

  def print_list(self):
    traversal = ""
    curr_node = self.root

    while curr_node != None:
      traversal += str(curr_node.data)
      curr_node = curr_node.next

    print(traversal)
    return traversal

  def find_element(self, element):
    curr_node = self.root

    while curr_node != None:
      if curr_node.data == element:
        return True
      curr_node = curr_node.next
    return False


root = Node(0)
first = Node(1)
second = Node(2)

root.next = first
first.next = second

ll1 = LinkedList(root)
ll1.print_list()
print(ll1.find_element(3))
