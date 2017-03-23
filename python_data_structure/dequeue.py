class Deque():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

    def __call__(self, *args, **kwargs):
        return self.items


s = Deque()
s.addFront(12)
s.addFront(14)
s.addFront(16)
s.addRear("fsd")

s.removeFront()

print(s())
