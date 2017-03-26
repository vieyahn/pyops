#Simple example
def toStr(n,base):
    converstring = '0123456789ABCDEF'
    if n < base:
        return converstring[n]
    else:
        return toStr(n//base,base) + converstring[n%base]
print(toStr(15,12))

# stack recursion

from Stack import Stack

s = Stack()
def ToStr(n,base):
    converstring = '0123456789ABCDEF'
    while n > 0:
        if n < base:
            s.push(converstring[n])
        else:
            s.push(converstring[n%base])
        n = n//base
    res = ''
    while not s.isEmpty():
        res = res + str(s.pop())
    return res
print(ToStr(1689879,2))