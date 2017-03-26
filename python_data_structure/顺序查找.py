
def sequentialSearch(alist,item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found

def orderSequentialSearch(alist,item):
    pos = 0
    found = False
    stop = False

    while pos<len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        elif alist[pos] > item:
            alist[pos] = True
        else:
            pos = pos + 1





