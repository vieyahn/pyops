def binarySearch(alist,item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found
testlist = [1,2,3,4,5,6,7,8,9,10]
print(binarySearch(testlist,3))
print(len(testlist))

'''

first = 0
last = 10-1 = 9


----------------
midpoint = 4
alist[4] = 5 > 3
last = 3
first = 0
----------------
midpoint = 1
alist[1] = 2 < 3
first = 2
last = 3
----------------
midpoint = 2
alist[2] = 3 == 3

'''

#递归二分查找 O(logN)
def dgbinarySearch(alist,item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:],item)
