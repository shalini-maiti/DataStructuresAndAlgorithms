class Queue():
  pos = { "regular": "reg", "reverse": "rev" }
  def __init__(self, obj=[]):
    self.obj = obj

  def enqueue(self, item, position = pos["regular"]):
    if position == self.pos["regular"]:
      self.obj.append(item)
    else:
      self.obj.append(item, 0)
    return self.obj

  def dequeue(self, position = pos["regular"]):
    if not self.is_empty():
      elem = self.obj.pop(0) if position == self.pos["regular"] else self.obj.pop(-1)
      return elem
    else:
      print("Queue is empty")


  def is_empty(self):
    return len(self.obj) == 0

  def peek(self, position = pos["regular"]):
    if not self.is_empty():
      elem = self.obj[0] if position == self.pos["regular"] else self.obj[-1]
      return elem
    else:
      print("Queue is empty")


if __name__ == "__main__":
  q = Queue()
  print(q.peek())
  print(q.dequeue())
  print(q.enqueue(1))
  print(q.enqueue(2))
  print(q.enqueue(3))
  print(q.dequeue())
  print(q.dequeue(position="rev"))
