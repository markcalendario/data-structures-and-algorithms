class Queue:
  def __init__(self):
    self.items = []

  def enqueue(self, value):
    self.items.append(value)

  def dequeue(self):
    self.items.pop(0)

  def getHead(self):
    return self.items[0]
  
  def getTail(self):
    return self.items[len(self.items)-1]

  def displayQueue(self):
    print(f"\033[92m" + str(self.items) + "\033[0m")

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

print(f"\u001b[31mAfter Queueing\033[0m")
queue.displayQueue()
print("Head: " + str(queue.getHead()))
print("Tail: " + str( queue.getTail()))
input("Press any key to continue.")

print("=============")

queue.dequeue()
print(f"\u001b[31mAfter Dequeueing\033[0m")
queue.displayQueue()
print("Head: " + str(queue.getHead()))
print("Tail: " + str( queue.getTail()))

print("=============")

queue.dequeue()
print(f"\u001b[31mAfter Dequeueing\033[0m")
queue.displayQueue()
print("Head: " + str(queue.getHead()))
print("Tail: " + str( queue.getTail()))


  