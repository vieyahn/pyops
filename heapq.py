import _heapq
# heap[0]永远是最小的数据

portfolio = [
{'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

#print heapq.nlargest(3,portfolio)

#cheap = heapq.nlargest(3,portfolio,key=lambda s:s['price'])
#expensive = heapq.nsmallest(3,portfolio,key=lambda s:s['price'])

nums = [1,8,2,23,-4,18,23,42,37,2]
_heapq.heapify(nums)
print(nums)
print(_heapq.heappop(nums))
print(_heapq.heappop(nums))
print(_heapq.heappop(nums))
print(nums)




#def heapify(nums):
 #   return None