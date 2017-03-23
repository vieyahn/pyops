class Queue():
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.insert(0,item)   # list's insert function
    def size(self):
        return len(len(self.items))
    def isEmpty(self):
        return self.items == []
    def dequeue(self):
        return self.items.pop()


