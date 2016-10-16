import _heapq

#怎样实现一个按优先级排序的队列?并且在这个队列上面每次 pop 操作总是返回 优先级最高的那个元素


class PriorityQueue:
    def __init__(self):
        self._queue=[]
        self._index=0


    def push(self,item,priority):
        _heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1

    def pop(self):
        return _heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self):
        self.name = name
    def __repr__(self):
        return "Item({!r})".format(self.name)

q = PriorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'),5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
q.pop()


