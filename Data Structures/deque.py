# Double ended queue, so deletionand insertion is possible on the front and the rear

class Deque:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def insertFront(self, item):
        self.items.insert(0, item)

    def insertRear(self, item):
        self.items.append(item)

    def removeFront(self):
        self.items.pop(0)

    def removeRear(self):
        self.items.pop()


dq = Deque()

print(dq.isEmpty())

dq.insertFront(77)
dq.insertRear(4)
dq.insertFront(56)

print(dq.size())
print(dq.items)

dq.removeFront()

print(dq.size())
print(dq.items)
print(dq.isEmpty())
