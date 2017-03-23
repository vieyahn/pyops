


def listsum(listnum):
    if len(listnum) == 1:
        return listnum[0]
    else:
        return listnum[0]+listsum(listnum[1:])

list1 = [2,3,1,4]
print(listsum(list1))