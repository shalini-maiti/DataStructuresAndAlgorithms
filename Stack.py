class Stack():
  def __init__(self, obj_list=[]):
    self.obj = obj_list

  def push(self, item):
    self.obj.append(item)
    return self.obj

  def pop(self):
    if not self.is_empty():
      elem = self.obj.pop()
      return elem
    else:
      print("Stack is empty")

  def peek(self):
    if not self.is_empty():
      elem = self.obj[-1]
      return elem
    else:
      print("Stack is empty")
    pass

  def is_empty(self):
    return len(self.obj) == 0

if __name__ == '__main__':
  st = Stack()
  print(st.pop())
  print(st.peek())
  print(st.push(1))
  print(st.push(2))
  print(st.pop())
  print(st.peek())

